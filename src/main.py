# necessary imports
from Game import Game

# create an instance of the game class 
game = Game()

# main method to run the game
def main():
    while game.IsRunning():
        game.Update()
        game.Render()
    game.Close()

# only execute the main func if this file is being run
if __name__ == "__main__":
    main()