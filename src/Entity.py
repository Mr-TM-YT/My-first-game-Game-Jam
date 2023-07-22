# This is a bass class for all the Entities in the game [Mr.TM]
import pygame as pg


# NOTE: This is an abstract class, don't make an instance of it
class Entity(pg.sprite.Sprite):
    def __init__(self, x=0, y=0) -> None:
        # We need to init pg.sprite.Sprite
        super().__init__()
        # Some basic vars
        self.x = x
        self.y = y
        self.width = 0  # Default width
        self.height = 0  # Default height
        self.vel = 0  # This is optional
        self.speed = 0  # Most entities will need a speed
        self.rect = None  # For collision
        self.image = None  # what will be shown on the screen

    # Called 60 times a second
    def update():
        pass

    # Will draw the Entity
    def render():
        pass
