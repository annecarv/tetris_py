from grid import Grid
from blocks import *
from block import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.game_paused = False
        self.score = 0

    def restart(self):
        self.grid.clear_grid()
        self.score = 0

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside_game_grid() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside_game_grid() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        if self.game_over == False:
            self.current_block.move(1, 0)
        if self.block_inside_game_grid() == False or self.block_fits() == False:
                self.current_block.move(-1, 0)
                self.lock_block()
        if self.game_over == True:
            self.current_block.move(-2, 0)

    def pause_game(self):
        self.game_paused = True

    def lock_block(self):
        if self.block_fits() == False and self.block_inside_game_grid() == True:
            self.game_over = True
        if self.block_fits() == True:
            tiles = self.current_block.get_cell_positions()
            for position in tiles:
                self.grid.grid[position.row][position.column] = self.current_block.id
            self.current_block = self.next_block
            self.next_block = self.get_random_block()
            self.grid.clear_full_rows()

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty_grid(tile.row, tile.column) == False:
                return False
        return True

    #Bloqueia o tretominó na grade e verifica se o mesmo não ultrapassou os limites dessa grade ao se movimentar
    def block_inside_game_grid(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside_grid(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self) :
        self.current_block.rotate()
        if self.block_inside_game_grid() == False or self.block_fits() == False:
            self.current_block.undo_rotation()

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
