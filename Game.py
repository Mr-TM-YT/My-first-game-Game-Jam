import pygame as pg
from Settings import *
# This is the game class that handles game initialization, update, and rendering


class Game:
    def __init__(self):
        # Init all Pygame modules
        pg.init()
        # Make the display (the window)
        self.display = pg.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))

        # checks if the game is running
        self.running = True
        # Sets the title for the window
        pg.display.set_caption(CAPTION)

        self.clock = pg.time.Clock()
        # Create a sprite group for the Player

    # Helps us to do the main game loop outside of Game
    def is_running(self):
        return self.running

    # Called 60 times a second
    def update(self, dt):
        # We're going modular so we'll have alot of functions, get used to that :)
        self.check_events()
        # Updating the player and giving it Delta Time so it's Framerate Independant

    # Renders everything on the window
    def render(self):
        # Fills the screen with blue, 'cuz yes
        self.display.fill((0, 0, 255))
        # Flips the buffer (Yeah I know some OpenGL baby)
        pg.display.flip()
        self.clock.tick(FPS)

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                # We'll just set running to False, so we can close later
                self.running = False

    # Clean everything (DON'T FORGET TO CALL IT)
    def close(self):
        pg.quit()
        exit()  # We call exit() so we can exit safely
