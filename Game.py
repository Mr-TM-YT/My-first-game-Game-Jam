import pygame as pg
from sys import exit
from Settings import *

pg.init()

class Game:
    # Start vars [Mr.TM]

    running = True
    display = None
    pg.display.set_caption("The (Team Name) is here baby")
    clock = pg.time.Clock()

    # Start temp [Mr.TM]

    keys = pg.key.get_pressed();

    # End temp [Mr.TM]

    # End vars [Mr.TM]

    # Start methods [Mr.TM]
    def __init__(self) -> None:
        self.Init() # Don't ask me why I made a seperate init function

    def IsRunning(self) -> bool: # This will help us do the main loop outside of the Game class [Mr.TM]
        return self.running;

    def Init(self) -> None: # the __init__ is not enough for me so I'll have a seperate init method [Mr.TM]
        self.display = pg.display.set_mode((WINDOW_SIZE["x"], WINDOW_SIZE["y"]), 32)

    def Update(self) -> None: # Called 60 times a second [Mr.TM]
        self.CheckEvents() # We're modular, You know [Mr.TM]


    def Render(self) -> None: # IDK but I felt adding this comment, Man the code is so concise and nice [Mr.TM]
        self.display.fill((0, 255, 0))

        # I will not make a seperate function just for drawing the "temp" player [Mr.TM]
        pg.draw.rect(self.display, square_color, (square_x,
                    square_y, square_size, square_size))
        
        pg.display.flip();
        self.clock.tick(60) # This should be in the Update but I'll put it in Render [Mr.TM]

    def CheckEvents(self) -> None: # I felt being modular today tbh [Mr.TM]
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False

    def Close(self):
        pg.quit()
        exit()
    
    
    # NOTE: HandleTempPlayerInput(slef) method doesn't work for some reason (I called it from the Update method don't worry) [Mr.TM]
    # TODO: Fix the HandleTempPlayerInput(self) method

    # def HandleTempPlayerInput(self): # Even if it will get deleted later, I have to make it modular [Mr.TM]
    #     if self.keys[pg.K_LEFT] or self.keys[pg.K_a]:
    #         square_x -= movement_speed
    #     if self.keys[pg.K_RIGHT] or self.keys[pg.K_d]:
    #         square_x += movement_speed
    #     if self.keys[pg.K_UP] or self.keys[pg.K_w]:
    #         square_y -= movement_speed
    #     if self.keys[pg.K_DOWN] or self.keys[pg.K_s]:
    #         square_y += movement_speed

    # End methods [Mr.TM]