import pyxel
from world import *

class Button:
    TextSize = [8, 16]
    ButtonSize = [40, 40]

    def __init__(self, x, y, lable, colkey = 14):
        self.x0 = x
        self.y0 = y
        self.label = lable
        self.colkey = colkey
        self.font = pyxel.Font("fonts/spleen-8x16.bdf")

    def show(self):
        pyxel.rect(self.x0, self.y0,
                   self.ButtonSize[0], self.ButtonSize[1],
                   self.colkey)
        xd = (self.ButtonSize[0] - self.TextSize[0]) / 2
        yd = (self.ButtonSize[1] - self.TextSize[1]) / 2
        pyxel.text(self.x0 + xd, self.y0 + yd, self.label, 1, self.font)
        pyxel.text(self.x0 + xd + 1, self.y0 + yd, self.label, 1, self.font)

    def pressed(self):
        if not pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            return False
        return (self.x0 <= pyxel.mouse_x and
                pyxel.mouse_x <= self.x0 + self.ButtonSize[0] and
                self.y0 <= pyxel.mouse_y and
                pyxel.mouse_y <= self.y0 + self.ButtonSize[1])

class Input:
    ButtonMargin = 10

    def __init__(self):
        pyxel.mouse(True)
        self.init_buttons()
        self.in_game = True
        self.a_pressed = False
        self.b_pressed = False
        self.x_pressed = False
        self.font = pyxel.Font("fonts/spleen-8x16.bdf")

    def init_buttons(self):
        margin = self.ButtonMargin
        x0 = margin
        y0 = g_world.screen_size.y - margin - Button.ButtonSize[1]
        self.button_b = Button(x0, y0, "B")
        x0 = g_world.screen_size.x - margin - Button.ButtonSize[0]
        self.button_a = Button(x0, y0, "A")
        x0 = (g_world.screen_size.x - Button.ButtonSize[0]) / 2 - Button.ButtonSize[0]
        self.button_x = Button(x0, y0, "X")
        
    def update(self, in_game):
        self.in_game = in_game
        self.a_pressed = False
        self.b_pressed = False
        self.x_pressed = False
        if (pyxel.btn(pyxel.GAMEPAD1_BUTTON_A) or
            pyxel.btn(pyxel.KEY_A)):
            self.a_pressed = True
        if (pyxel.btn(pyxel.GAMEPAD1_BUTTON_B) or
            pyxel.btn(pyxel.KEY_B)):
            self.b_pressed = True
        if (pyxel.btn(pyxel.GAMEPAD1_BUTTON_X) or
            pyxel.btn(pyxel.KEY_X)):
            self.x_pressed = True
        if self.button_a.pressed():
            self.a_pressed = True
        if self.button_b.pressed():
            self.b_pressed = True
        if self.button_x.pressed():
            self.x_pressed = True

    def show(self):
        if self.in_game:
            self.button_a.show()
            self.button_b.show()
            self.button_x.show()
            margin = self.ButtonMargin
            x0 = (g_world.screen_size.x - Button.ButtonSize[0]) / 2 + margin
            y0 = g_world.screen_size.y - margin - (Button.ButtonSize[1] - Button.TextSize[1]) / 2 - Button.TextSize[1]
            pyxel.text(x0, y0, "Retry", 1, self.font)
        else:
            self.button_x.show()
