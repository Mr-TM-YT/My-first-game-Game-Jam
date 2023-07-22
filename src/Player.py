import pygame as pg
from Entity import Entity
from Settings import WINDOW_SIZE, square_size


# This is the player class derived from the Entity class
class Player(Entity):
    def __init__(self, x, y, speed):
        super().__init__()
        self.x = x
        self.y = y
        self.vel = 0
        self.speed = speed
        self.image = pg.Surface((square_size, square_size))
        self.image.fill((255, 165, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.gravity = 1
        self.jump_power = -18
        self.is_jumping = False
        self.is_on_ground = False
        self.can_jump = True
        self.max_jump_height = 100

    def update(self):
        self.move()
        self.apply_gravity()
        self.check_boundary()
        self.handle_jumping()

    def move(self):
        keys = pg.key.get_pressed()
        if (keys[pg.K_LEFT] or keys[pg.K_a]) and self.x >= 0:
            self.x -= self.speed
        if (keys[pg.K_RIGHT] or keys[pg.K_d]) and self.x <= WINDOW_SIZE["x"] - square_size:
            self.x += self.speed

    def apply_gravity(self):
        if not self.is_jumping:
            self.vel += self.gravity
        self.y += self.vel

    def check_boundary(self):
        if self.y >= WINDOW_SIZE["y"] - square_size:
            self.y = WINDOW_SIZE["y"] - square_size
            self.vel = 0
            self.is_on_ground = True
            self.is_jumping = False
            self.can_jump = True

    def handle_jumping(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.is_on_ground and self.can_jump:
            self.is_jumping = True
            self.is_on_ground = False
            self.vel = self.jump_power
            self.can_jump = False

        if self.is_jumping:
            self.y += self.vel
            self.vel += self.gravity

            if self.y <= WINDOW_SIZE["y"] - square_size - self.max_jump_height:
                self.is_jumping = False

        if not self.is_jumping and self.y == WINDOW_SIZE["y"] - square_size:
            self.is_on_ground = True

    def render(self, display):
        display.blit(self.image, (self.x, self.y))
