from game import Game
from colors import Colors
import pygame, sys

pygame.init()
game = Game()

#Game window
title_font = pygame.font.SysFont('calibri', 35)
next_font = pygame.font.SysFont('calibri', 35)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = next_font.render("Next", True, Colors.white)
game_over_surface = next_font.render("Game Over!", True, Colors.white)
score_rect = pygame.Rect(320, 50, 170, 90)
next_rect = pygame.Rect(320, 210, 170, 180)
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
                game.game_over = False
                game.restart()
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
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)

    screen.blit(score_surface, (360, 10, 50, 50))
    screen.blit(next_surface, (365, 160, 40, 40))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.dark_grey, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
		centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.dark_grey, next_rect, 0, 10)

    game.draw(screen)

    pygame.display.update()
    #Taxa de quadros - FPS
    clock.tick(60)