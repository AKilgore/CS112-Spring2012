import pygame

from game import Game

def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 800))

    # create game
    game = Game(screen)
    try:
        app.run()
    except KeyboardInterrupt:
        app.quit()

if __name__ == "__main__":
    main()
