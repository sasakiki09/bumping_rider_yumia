import pyxel
import random
from game_constants import *
from world import *
from physics import *
from utilities import *

class GameBike:
    def __init__(self,
                 bike_body_path, tire_path, chara_body_path,
                 gray_converter = None):
        self.bike = Bike()
        self.width = BikeSpriteWidth
        self.height = BikeSpriteHeight
        self.next_blink_tic = 20
        self.chara_body_index = CharaBodyIndex.Normal
        self.gray_converter = gray_converter
        self.set_sprite_ranges()

        self.bike_body_image = self.clip_image(
            self.load(bike_body_path),
            self.bike_body_range)
        self.tire_image = self.clip_image(
            self.load(tire_path),
            self.tire_range)
        self.chara_body_image = self.clip_image(self.load(chara_body_path))

    def load(self, path):
        image = pyxel.Image(256, 256)
        image.load(0, 0, path)
        return image

    def set_sprite_ranges(self):
        w = BikeSpriteWidth
        h = BikeSpriteHeight
        self.bike_body_range = Range2(0, 0, w, h)
        self.chara_body_range_0 = Range2(0, 0, w, h)
        self.chara_body_range_1 = Range2(0, h, w, h)
        self.chara_body_range_steer = Range2(0, h * 2, w, h)
        self.chara_body_range_cry = Range2(0, h * 3, w, h)
        r = BikeSpriteHeight // 4
        self.tire_range = Range2(0, r * 2, r * 2, r * 2)
        self.front_tire_center = Vec2(w / 2 - r, r)
        self.rear_tire_center = Vec2(-w / 2 + r, r)

    def clip_image(self, image, range = None):
        util = ImageUtils(image, range)
        return util.clipped(self.gray_converter)

    def screen_xy(self):
        w_loc = self.bike.location
        s_loc = g_world.screen_xy(w_loc)
        return Vec2(s_loc.x - self.width / 2,
                    s_loc.y - self.height / 2)

    def rotation_degree(self):
        rotation = self.bike.rotation
        return -180.0 / math.pi * rotation

    def tire_rotation_degree(self):
        r = BikeWorldLen / 6
        l = math.pi * 2 * r
        ratio = (self.bike.location.x % l) / l
        return 180.0 * ratio

    def chara_body_range(self):
        if self.chara_body_index == CharaBodyIndex.Succeeded:
            return self.chara_body_range_steer
        if self.chara_body_index == CharaBodyIndex.Failed:
            return self.chara_body_range_cry
        if self.bike.rotation_velocity < 0:
            return self.chara_body_range_0
        else:
            return self.chara_body_range_1
        
    def show(self):
        s_xy = self.screen_xy()
        rot = self.rotation_degree()
        r = self.tire_range
        f_rel = self.front_tire_center.rotate(-self.bike.rotation)
        f_xy = s_xy + f_rel + self.front_tire_center
        tire_rot = self.tire_rotation_degree()
        pyxel.blt(f_xy.x, f_xy.y, self.tire_image,
                  0, 0, r.w, r.h,
                  g_world.bg_index,
                  tire_rot)
        r_rel = self.rear_tire_center.rotate(-self.bike.rotation)
        r_xy = s_xy + r_rel + self.front_tire_center
        pyxel.blt(r_xy.x, r_xy.y, self.tire_image,
                  0, 0, r.w, r.h,
                  g_world.bg_index,
                  tire_rot)
        r = self.bike_body_range
        pyxel.blt(s_xy.x, s_xy.y, self.bike_body_image,
                  0, 0, r.w, r.h,
                  g_world.bg_index,
                  rot)
        r = self.chara_body_range()
        pyxel.blt(s_xy.x, s_xy.y, self.chara_body_image,
                  r.x, r.y, r.w, r.h,
                  g_world.bg_index,
                  rot)
        
    def update(self, ground, btn_a, btn_b):
        self.bike.update(ground, btn_a, btn_b)
        self.chara_body_index = CharaBodyIndex.Normal

    def update_chara_body_index(self, index):
        self.chara_body_index = index

    def failed(self):
        return self.bike.failed()

    def face_index(self):
        if abs(math.sin(self.bike.rotation)) > 0.65:
            return FaceIndex.Astonish
        if g_world.tic % self.next_blink_tic == 0:
            return FaceIndex.Blink
        elif g_world.tic % self.next_blink_tic == 1:
            self.next_blink_tic = random.randint(10, 30)
            return FaceIndex.Blink
        else:
            return FaceIndex.Normal
