# importing necessary stuff
import pygame as pg
from sys import exit

# necessary variables
screen = pg.display.set_mode((800, 600), 32)
pg.display.set_caption("Game")
clock = pg.time.Clock()
running = True

# game loop
while running:
    # checking for updates
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            exit()
            
    # drawing stff goes here

    # updating the screen and limiting the fps to 60
    pg.display.flip()
    clock.tick(60)
