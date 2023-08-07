import pygame, sys
from colors import Colors
from grid import Grid

pygame.init()

#Game window
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

#Velocidade do jogo
clock = pygame.time.Clock()

game_grid = Grid()
game_grid.print_grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Drawing
    screen.fill(Colors.dark_blue)

    game_grid.draw(screen)
    pygame.display.update()
    #Taxa de quadros - FPS
    clock.tick(60)