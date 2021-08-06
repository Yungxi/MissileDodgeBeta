import pygame
import config
from game_state import GameState
from game import Game

#All initializations
pygame.init()

#Setting window
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

#setting caption
pygame.display.set_caption("Missile Dodge")

#setting lcock
clock = pygame.time.Clock()

#creating game object
game = Game(screen)
game.set_up()

#while game is runing, refresh screen 50 frames per second
while game.game_state == GameState.RUNNING:
    clock.tick(50)
    game.update()
    pygame.display.flip()