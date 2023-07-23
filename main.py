from Game import Game
import pygame as pg

# This is the main function to run the game


def main():
    game = Game()
    while game.is_running():
        game.update(pg.time.Clock().tick(60) / 1000.0)  # Delta time
        game.render()    # Draws everything

    game.close()  # Cleans everything


if __name__ == "__main__":
    main()
