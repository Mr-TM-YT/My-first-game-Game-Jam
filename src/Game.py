import pygame as pg
from Settings import WINDOW_SIZE, movement_speed
from Player import Player


# This is the game class that handles game initialization, update, and rendering
class Game:
    def __init__(self):
        self.init()
        self.player = Player(
            WINDOW_SIZE["x"] // 2, WINDOW_SIZE["y"] // 2, movement_speed)

    def is_running(self):
        return self.running

    def init(self):
        pg.init()
        self.display = pg.display.set_mode(
            (WINDOW_SIZE["x"], WINDOW_SIZE["y"]))
        self.running = True
        self.clock = pg.time.Clock()
        pg.display.set_caption("The (Team Name) is here baby")

    def update(self):
        self.check_events()
        self.player.update()

    def render(self):
        self.display.fill((0, 0, 255))
        self.player.render(self.display)
        pg.display.flip()
        self.clock.tick(60)

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False

    def close(self):
        pg.quit()
        exit()
