import pygame as pg


# This is the base class for all entities in the game
class Entity(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.vel = 0
        self.speed = 0
        self.rect = None
        self.image = None
