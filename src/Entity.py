# This is a bass class for all the Entities in the game [Mr.TM]
import pygame as pg


class Entity(pg.sprite.Sprite):
    def __init__(self, x=0, y=0, speed=0) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = None
        self.image = None

    def Update():
        pass

    def Render():
        pass
