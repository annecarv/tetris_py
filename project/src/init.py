from game import Game
from colors import Colors
import pygame, sys

pygame.init()
game = Game()

#Game window
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

#Velocidade do jogo - Ajustar depois de acordo com os níveis
clock = pygame.time.Clock()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.restart()
                game.game_over = False
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()
    #Drawing
    screen.fill(Colors.dark_blue)
    game.draw(screen)

    pygame.display.update()
    #Taxa de quadros - FPS
    clock.tick(60)