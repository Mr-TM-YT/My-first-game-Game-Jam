from Game import Game


# This is the main function to run the game
def main():
    game = Game()

    while game.is_running():
        game.update()
        game.render()

    game.close()


if __name__ == "__main__":
    main()
