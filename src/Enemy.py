from Entity import Entity
from Settings import *
import pygame as pg


# This is the enemy class (maybe other enemies will be derived from him)
class Enemy(Entity):
    # init method (should take a refrence to the display)
    def __init__(self, display):
        self.width = 50
        self.height = 50
        self.vel = 1
        self.speed = 10
        super().__init__(
            WINDOW_SIZE["x"] / 2 - self.width / 2, WINDOW_SIZE["y"] / 2 - self.height)
        self.display = display  # Yeah a pointer to a display :)

    def do_ai_stuff(self):
        if self.x >= WINDOW_SIZE["x"] - self.width or self.x <= 0:
            self.vel *= -1

        self.x += self.x * self.vel

    def update(self) -> None:
        self.do_ai_stuff()
        print(f"X for the enemy is: {self.x}")
        print(f"Y for the enemy is {self.y}")

    def render(self) -> None:
        pg.draw.rect(self.display, (0, 255, 0),
                     (self.x, self.y, self.width, self.height))
