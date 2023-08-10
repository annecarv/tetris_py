import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        #Lista de compreensão
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors =  Colors.get_cell_colors()

    """
    #Apenas para ilustrar como as grades com as linhas são criadas
    def print_grid(self):
    for row in range(self.num_rows):
        for column in range(self.num_cols):
            print(self.grid[row][column], end = " " )
        print()
    """
    #Verifica os limites das grades (utilizado para evitar de algum bloco de ultrapassar esse limite)
    def is_inside_grid(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    #Verifica se o campo no grid esta vazio
    def is_empty_grid(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        for column in range (self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        for column in range (self.num_cols):
            self.grid[row][column] == 0

    def clear_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    #....Move as linhas para baixo, mas nao consegui entender bem a lógica
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    #Limpa a linha mas tb nao entendi
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    #Desenha o retangulo do jogo com suas respectivas linhas e colunas formando as grades
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                #cell_rect = pygame.Rect(x, y, w, h)
                cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11,
                self.cell_size - 1, self.cell_size - 1)
                #pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)