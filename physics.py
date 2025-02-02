from world import *
import math
from enum import Enum, auto

class Wheel(Enum):
    Front = auto()
    Rear = auto()

class Coordinate(Enum):
    World = auto()
    Local = auto()

# -x: front, +x: rear
# -y: down,  +y: up
class Location(Vec2):
    def __init__(self):
        self.coordinate = False
        self.x = False
        self.y = False

    def __init__(self, coord, x, y):
        self.coordinate = coord
        self.x = x
        self.y = y

    def __str__(self):
        return "Location(%s,%f,%f)" % (self.coordinate, self.x, self.y)

class Bike:
    def __init__(self):
        self.length = BikeWorldLen
        self.min_height = 0.02
        self.reset()
        self.acceleration = 8.0 # m/s^2
        self.max_speed = 28.0 # m/s
        self.speed_decay = 0.02
        self.reflection = 0.3
        l = self.length
        self.front_wheel_center = Vec2(l * 3 / 8, -l / 8)
        self.rear_wheel_center = Vec2(-l * 3 / 8, -l / 8)
        self.wheel_radius = l / 5

    def reset(self):
        self.location = Vec2(0.0, 2.0)
        self.velocity = Vec2(0.0, 0.0)
        self.rotation = 0.0 # radian
        self.rotation_velocity = 0.0
        self.touched = False
        self.last_touched = False
        
    def speed_ratio(self):
        return (self.velocity.x / self.max_speed)

    def to_local(self, location):
        if location.coordinate == Coordinate.Local:
            return location
        if location.coordinate != Coordinate.World:
            raise
        lxy = (location - self.location).rotate(-self.rotation)
        return Location(Coordinate.Local, lxy.x, lxy.y)

    def to_world(self, location):
        if location.coordinate == Coordinate.World:
            return location
        if location.coordinate != Coordinate.Local:
            raise
        rxy = location.rotate(self.rotation)
        wxy = rxy + self.location
        return Location(Coordinate.World, wxy.x, wxy.y)

    def wheel_center(self, wheel):
        if wheel == Wheel.Front:
            wcenter = self.front_wheel_center
        elif wheel == Wheel.Rear:
            wcenter = self.rear_wheel_center
        else:
            raise
        return Location(Coordinate.Local, wcenter.x, wcenter.y)

    def wheel_height(self, wheel, ground):
        wcenter = self.wheel_center(wheel)
        wwcenter = self.to_world(wcenter)
        gh = ground.height(wwcenter.x)
        return (wwcenter.y - self.wheel_radius) - gh
    
    def wheel_is_on_ground(self, wheel, ground):
        return (self.wheel_height(wheel, ground) <= self.min_height)

    def height_from_ground(self, ground):
        h_f = self.wheel_height(Wheel.Front, ground)
        h_r = self.wheel_height(Wheel.Rear, ground)
        return min(h_f, h_r)

    def update_velocity(self, ground, btn_a, btn_b):
        self.velocity.x -= self.speed_decay
        f_h = self.wheel_height(Wheel.Front, ground)
        r_h = self.wheel_height(Wheel.Rear, ground)
        f_touch = (f_h <= self.min_height)
        r_touch = (r_h <= self.min_height)
        if self.last_touched and not (f_touch or r_touch):
            self.last_touched = False
            if f_h < r_h:
                f_touch = True
            else:
                r_touch = True
        dt = world.delta_time
        self.touched = (f_touch or r_touch)
        if (f_touch or r_touch):
            self.velocity.y = self.reflection * abs(self.velocity.y)
        elif not (f_touch and r_touch):
            self.velocity += world.gravity.mul(dt)
        rot_acc = math.pi / 3
        if f_touch and not btn_b:
            self.rotation_velocity += rot_acc * dt
        if r_touch and not btn_a:
            self.rotation_velocity -= rot_acc * dt
        if btn_a and self.velocity.x < self.max_speed and r_touch:
            self.velocity.x += self.acceleration * dt * math.cos(self.rotation)
            self.rotation_velocity += rot_acc *  dt
        if btn_b and self.velocity.x > 0.0:
            self.rotation_velocity -= rot_acc * dt
            if f_touch:
                self.velocity.x -= self.acceleration * dt
            else:
                self.velocity.x -= self.acceleration * dt * 0.3
        self.velocity.x = max(0.0, self.velocity.x)
        self.velocity.x = min(self.max_speed, self.velocity.x)

    def update(self, ground, btn_a, btn_b):
        self.update_velocity(ground, btn_a, btn_b)
        h = self.height_from_ground(ground)
        self.location += self.velocity.mul(world.delta_time)
        self.rotation += self.rotation_velocity * world.delta_time
        if h < 0.0:
            self.location.y += -h
            self.last_touched = True

    def failed(self):
        return (self.touched and math.cos(self.rotation) <= 0)
    
class Ground:
    def __init__(self):
        self.coords = []
        self.last_index = False

    def __init__(self, coords):
        self.coords = sorted(coords, key=lambda c: c.x)
        if len(self.coords) < 2: raise
        self.last_index = False

    def height(self, x):
        index = Vec2.find_index(self.coords, x, self.last_index)
        if (x < self.coords[0].x or self.coords[-1].x < x):
            return False
        if index == len(self.coords) - 1:
            return self.coords[index].y
        x0 = self.coords[index].x
        y0 = self.coords[index].y
        x1 = self.coords[index + 1].x
        y1 = self.coords[index + 1].y
        if not (x0 <= x and x <= x1):
            print('x0:%f x1:%f x:%f' % (x0, x1, x))
            raise
        if x0 == x1: raise
        return y0 + (y1 - y0) / (x1 - x0) * (x - x0)

    def goal_x(self):
        return self.coords[-1].x
