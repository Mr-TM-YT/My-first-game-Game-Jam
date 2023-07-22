# necessary imports
import pygame as pg
from sys import exit
from Settings import *

# initialize pygame
pg.init()


class Game:
    #  necessary variables
    running = True
    display = None
    pg.display.set_caption("The (Team Name) is here baby")
    clock = pg.time.Clock()
    keys = pg.key.get_pressed()

    #  init method
    def __init__(self) -> None:
        self.Init()
        # Initial x position of the square
        self.square_x = WINDOW_SIZE["x"] // 2
        # Initial y position of the square
        self.square_y = WINDOW_SIZE["y"] // 2

    # checks if the game is running
    def IsRunning(self) -> bool:
        return self.running

    # idk why another init 🤔
    def Init(self) -> None:
        self.display = pg.display.set_mode(
            (WINDOW_SIZE["x"], WINDOW_SIZE["y"]))

    # update the game
    def Update(self) -> None:
        self.CheckEvents()

    # draw stff on the screen
    def Render(self) -> None:
        self.display.fill((0, 0, 255))
        pg.draw.rect(self.display, square_color, (self.square_x,
                                                  self.square_y, square_size, square_size))
        pg.display.flip()
        self.clock.tick(60)

    # check for events
    def CheckEvents(self) -> None:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False

        # Update keys state on each iteration
        self.keys = pg.key.get_pressed()

        # Now use self.square_x and self.square_y to update the position
        if self.keys[pg.K_LEFT] or self.keys[pg.K_a]:
            self.square_x -= movement_speed
        if self.keys[pg.K_RIGHT] or self.keys[pg.K_d]:
            self.square_x += movement_speed
        if self.keys[pg.K_UP] or self.keys[pg.K_w]:
            self.square_y -= movement_speed
        if self.keys[pg.K_DOWN] or self.keys[pg.K_s]:
            self.square_y += movement_speed

    # close the game and cleanup
    def Close(self):
        pg.quit()
        exit()
