# # importing necessary stuff
# import pygame as pg
# from sys import exit

# # necessary variables
# screen = pg.display.set_mode((800, 600))
# pg.display.set_caption("Game")
# clock = pg.time.Clock()
# running = True
# # temp player code
# square_size = 50
# square_color = (255, 0, 0)  # square color "red"
# square_x, square_y = 800 // 2 - square_size, 600 // 2 - \
#     square_size  # position of the square center of the screen
# movement_speed = 5  # movement speed of the square

# # game loop
# # Making a def makes you sexy [Mr.TM]

# while running:
#     # checking for updates
#     for e in pg.event.get():
#         if e.type == pg.QUIT:
#             pg.quit()
#             exit()

#     # get the state of the keys (pressed/released)
#     keys = pg.key.get_pressed()

#     # movement for the player
#     if keys[pg.K_LEFT] or keys[pg.K_a]:
#         square_x -= movement_speed
#     if keys[pg.K_RIGHT] or keys[pg.K_d]:
#         square_x += movement_speed
#     if keys[pg.K_UP] or keys[pg.K_w]:
#         square_y -= movement_speed
#     if keys[pg.K_DOWN] or keys[pg.K_s]:
#         square_y += movement_speed

#     # drawing stff goes here
#     screen.fill((255, 255, 255))
#     pg.draw.rect(screen, square_color, (square_x,
#                 square_y, square_size, square_size))

#     # updating the screen and limiting the fps to 60
#     pg.display.flip()
#     clock.tick(60)

from Game import Game

game = Game()

def main():
    while game.IsRunning():
        game.Update()
        game.Render()
    game.Close()


if __name__ == "__main__":
    main()