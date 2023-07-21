import pygame as pg
from sys import exit

screen = pg.display.set_mode((800, 600), 32)
pg.display.set_caption("Game")
clock = pg.time.Clock()
running = True

while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.flip()
    clock.tick(60)
