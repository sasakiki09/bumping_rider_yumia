from world import *
import math
from enum import Enum

class Wheel(Enum):
    Front = 0
    Rear = 1

class Coordinate(Enum):
    World = 0
    Local = 1

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
        self.location = Vec2(0.0, 0.0)
        self.velocity = 0.0
        self.rotation = 0.0 # radian
        self.rotation_velocity = 0.0
        self.mass = 100.0 # kg
        l = self.length
        self.front_wheel_center = Vec2(-l * 3 / 8, -l / 8)
        self.rear_wheel_center = Vec2(l * 3 / 8, -l / 8)
        self.wheel_radius = l / 8

    def get_location(self):
        return self.location

    def set_location(self, x, y):
        self.location = Vec2(x, y)

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
    
    def wheel_is_on_ground(self, wheel, ground):
        wcenter = self.wheel_center(wheel)
        wwcenter = self.to_world(wcenter)
        gh = ground.height(wwcenter.x)
        return (gh >= wwcenter.y - self.wheel_radius)
    
class Ground:
    def __init__(self):
        self.coords = []
        self.last_index = False

    def __init__(self, coords):
        self.coords = sorted(coords, key=lambda c: c.x)
        if len(self.coords) < 2: raise
        self.last_index = False

    # Find minmum index such that self.coords[index] <= x.
    def find_index(self, x):
        if not self.last_index: self.last_index = 0
        index = self.last_index
        while (index < len(self.coords) - 1 and
               self.coords[index].x < x):
            index += 1
        while (0 < index and
               x < self.coords[index].x):
            index -= 1
        return index
        
    def height(self, x):
        index = self.find_index(x)
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

if __name__ == '__main__':
    # Ground Test
    ground = Ground([Vec2(0.0, 1.0), Vec2(10.0, 15.0)])
    for x in range(20):
        y = ground.height(x)
        print('x: %f, y: %f' % (x, y))

    # Bike Test
    bike = Bike()
    bike.set_location(5.0, 20.0)
    print('Bike is on ground: %d %d' %
          (bike.wheel_is_on_ground(Wheel.Front, ground),
           bike.wheel_is_on_ground(Wheel.Rear, ground)))
    bike.set_location(5.0, 8.0)
    print('Bike is on ground: %d %d' %
          (bike.wheel_is_on_ground(Wheel.Front, ground),
           bike.wheel_is_on_ground(Wheel.Rear, ground)))
    bike.set_location(5.0, 6.0)
    print('Bike is on ground: %d %d' %
          (bike.wheel_is_on_ground(Wheel.Front, ground),
           bike.wheel_is_on_ground(Wheel.Rear, ground)))
    
