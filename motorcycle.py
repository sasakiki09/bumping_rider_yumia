import pyxel

ScreenSize = [240, 180]
Title = "Yumia Motor Dash"
BGIndex = 0

FrontWheel = 0
RearWheel = 1

class Player:
    def __init__(self, image_index):
        self.width = 48
        self.height = 32
        self.wheel_radius = 8
        self.front_wheel_center = [12, 8]
        self.rear_wheel_center = [8, 8]
        self.image_index = image_index
        self.x = ScreenSize[0] / 2
        self.y = ScreenSize[1] / 2
        self.rotation = 0
        self.load()
        self.set_wheels()

    def load(self):
        self.image = pyxel.images[self.image_index]
        self.image.load(0, 0, "images/player.png")

    def set_wheels(self):
        y1 = self.height - 1
        bounds = []
        last_on_wheel = False
        for x in range(self.width):
            on_wheel = (self.image.pget(x, y1) != BGIndex)
            if on_wheel != last_on_wheel:
                bounds.append(x)
        if len(bounds) < 4: raise
        self.rear_wheel = [bounds[0], bounds[1] - 1]
        self.front_wheel = [bounds[2], bounds[3] - 1]

    def wheel_is_on_ground(self, wheel, ground):
        if len(wheel) != 2: raise
        # working 2025.01.05
        # 回転も考えるのなら車輪の中心と距離で
        # 判定すべきでは? 
        pass
    
    def show(self):
        x = self.x - self.width / 2
        y = self.y - self.height / 2
        pyxel.blt(x, y, self.image_index,
                  0, 0, self.width, self.height,
                  BGIndex,
                  self.rotation)

class Ground:
    pass

class App:
    def __init__(self):
        pyxel.init(ScreenSize[0], ScreenSize[1], Title)
        self.player = Player(0)
        self.tic = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.tic += 1
        self.player.rotation = self.tic % 360
        self.input()

    def draw(self):
        pyxel.cls(13)
        self.player.show()

    def input(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.x += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.player.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.player.y += 1

App()

