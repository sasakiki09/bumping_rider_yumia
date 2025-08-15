import pyxel
import random
from game_constants import *
from color_palette import *
from world import *
from physics import *
from stages import *
from background import *
from input import *
from play_record import *
from face import *
from status import *
from title import *
from result import *
from game_result import *
from sound import *
from music import *
from game_bike import GameBike

class GameGround:
    def ground(self):
        return g_stages[g_world.stage_index].ground

    def screen_y(self, screen_x):
        w_xy = g_world.world_xy(Vec2(screen_x, 0))
        w_y = self.ground().height(w_xy.x)
        s_xy = g_world.screen_xy(Vec2(w_xy.x, w_y))
        s_y = s_xy.y
        on_course = (w_xy.x <= self.ground().goal_x())
        return (s_xy.y, on_course)

    def color_index(self, screen_x):
        w_x = g_world.world_xy(Vec2(screen_x, 0)).x
        x = int(w_x) % 10
        if x < 5:
            return ColorPalette.Ground0
        else:
            return ColorPalette.Ground1

    def show(self):
        for x in range(g_world.screen_size.x):
            y, on_course = self.screen_y(x)
            if on_course:
                col = self.color_index(x)
            else:
                col = ColorPalette.GroundGoal
            pyxel.line(x, y, x, g_world.screen_size.y, col)
            pyxel.line(x, y + g_world.rival_diff, x, y, ColorPalette.GroundSurface)

class App:
    BikeBodyImagePath = 'images/bike_body.png'
    TireImagePath = 'images/tire.png'
    CharaBodyImagePath = 'images/chara_body.png'
    FacesImagePath = 'images/faces.png'
    TitleCharaImagePath = 'images/title_chara.png'
    TitleTextImagePath = 'images/title_text.png'
    ResultCharaImagePath = 'images/result_chara.png'
    
    def __init__(self):
        pyxel.init(g_world.screen_size.x,
                   g_world.screen_size.y,
                   g_world.title,
                   fps = g_world.fps)
        self.color_palette = ColorPalette(
            [self.BikeBodyImagePath,
             self.TireImagePath,
             self.CharaBodyImagePath],
            [self.FacesImagePath,
             self.TitleCharaImagePath,
             self.TitleTextImagePath,
             self.ResultCharaImagePath])
        self.state = GameState.GameTitle
        self.title = Title(
            self.TitleCharaImagePath,
            self.TitleTextImagePath)
        self.game_result = GameResult(self.ResultCharaImagePath)
        self.bike = GameBike(
            self.BikeBodyImagePath,
            self.TireImagePath,
            self.CharaBodyImagePath)
        self.bike_rival = GameBike(
            self.BikeBodyImagePath,
            self.TireImagePath,
            self.CharaBodyImagePath,
            self.color_palette.gray_converter())
        self.ground = GameGround()
        g_world.start()
        self.input = Input()
        self.play_record = PlayRecord()
        self.play_record_rival = None
        self.face = Face(image_index = 1, path = self.FacesImagePath)
        self.status = Status()
        self.result = Result()
        self.sound = Sound(sound_index = 0)
        self.music = Music(sound_index = 1)
        self.reset()
        pyxel.run(self.update, self.draw)

    def stage(self):
        return g_stages[g_world.stage_index]

    def bike_x_diff(self):
        diff_max = g_world.origin_screen.x
        v_max = self.bike.bike.max_speed
        v = self.bike.bike.velocity.x
        return v / v_max * diff_max / g_world.scale.x

    def goal_distance(self):
        return self.stage().ground.goal_x() - self.bike.bike.location.x

    def update_face(self, in_game, succeeded):
        if in_game:
            self.face.update(self.bike.face_index())
        else:
            if succeeded:
                self.face.update(FaceIndex.Smile)
            else:
                self.face.update(FaceIndex.Cry)

    def update_in_game(self):
        self.background.update(g_world.origin_world.x)
        bike = self.bike.bike
        ox = bike.location.x + self.bike_x_diff()
        tic = g_world.tic
        g_world.update(Vec2(ox, 0))
        self.input.update(True)
        btn_a = self.input.a_pressed
        btn_b = self.input.b_pressed
        self.play_record.add(btn_a, btn_b)
        self.bike.update(self.stage().ground, btn_a, btn_b)
        if self.play_record_rival:
            btn_r = self.play_record_rival.recorded_buttons(tic)
            self.bike_rival.update(self.stage().ground, btn_r[0], btn_r[1])
        self.status.update(self.bike.bike, self.stage().ground)
        self.update_face(True, False)
        self.result.update(False, False)
        if self.input.x_pressed:
            self.reset()

    def update_result(self, failed, result_time):
        self.input.update(False)
        if failed:
            self.bike.update_chara_body_index(CharaBodyIndex.Failed)
        else:
            self.bike.update_chara_body_index(CharaBodyIndex.Succeeded)
        self.result.update(failed, result_time)
        self.update_face(False, not failed)
        if self.input.x_pressed:
            if result_time:
                stage = self.stage()
                stage_index = g_world.stage_index
                stage.update_best_time(stage_index, result_time, self.play_record)
                s_i = (stage_index + 1) % len(g_stages)
                g_world.stage_index = s_i
                if s_i == 0:
                    self.state = GameState.GameResult
                    self.game_result.reset()
            self.reset()

    def update(self):
        if self.state == GameState.GameTitle:
            self.title.update()
            if self.title.start_pressed():
                self.state = GameState.GamePlay
                self.reset()
        elif self.state == GameState.GamePlay:
            failed = self.bike.failed()
            if self.goal_distance() <= 0:
                result_time = g_world.elapsed_time
            else:
                result_time = False
            if failed or result_time:
                self.music.stop()
                self.update_result(failed, result_time)
                self.sound.update(False)
            else:
                self.update_in_game()
                self.sound.update(self.bike.bike.speed_ratio())
        elif self.state == GameState.GameResult:
            self.game_result.update()
            if self.game_result.pressed():
                self.to_title()
        else:
            raise

    def draw(self):
        if self.state == GameState.GameTitle:
            self.title.show()
        elif self.state == GameState.GamePlay:
            self.background.show()
            self.ground.show()
            if self.play_record_rival:
                self.bike_rival.show()
            self.bike.show()
            self.input.show()
            self.face.show()
            self.status.show()
            self.result.show()
        elif self.state == GameState.GameResult:
            self.game_result.show()
        else:
            raise

    def reset(self):
        g_world.start()
        index = g_world.stage_index
        self.stage().start()
        self.background = Background()
        self.play_record.reset()
        if g_savedata.record_a(index):
            rec_a = g_savedata.record_a(index)
            rec_b = g_savedata.record_b(index)
            self.play_record_rival = PlayRecord(rec_a, rec_b)
        else:
            self.play_record_rival = None
        self.bike.bike.reset()
        self.bike_rival.bike.reset()
        if self.state == GameState.GamePlay:
            self.music.play(self.stage().music)
        else:
            self.music.play(4)

    def to_title(self):
        self.title.reset()
        self.state = GameState.GameTitle
        self.reset()
        
App()
