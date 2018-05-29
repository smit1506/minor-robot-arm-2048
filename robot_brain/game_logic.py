import numpy as np
from numpy import array, zeros, rot90
from random import randint, random

class Board_game_2048():
    def __init__(self):
        self.board = zeros((4, 4), dtype=np.int)
        self.game_over = False
        
    def move(self, direction):
        pass
    
    def is_game_over(self):
        pass

score = 0

def fill_cell(board):
    i, j = (board == 0).nonzero()
    if i.size != 0:
        rnd = randint(0, i.size - 1)
        board[i[rnd], j[rnd]] = 2 * ((random() > .9) + 1)

def move(board, direction):
    # 0: left, 1: up, 2: right, 3: down
    rotated_board = rot90(board, direction)
    cols = [rotated_board[i, :] for i in range(4)]
    new_board = array([move_left(col) for col in cols])
    return rot90(new_board, -direction)

def move_left(col):
    new_col = zeros((4), dtype=col.dtype)
    j = 0
    global score
    new_score = score
    previous = None
    for i in range(col.size):
        if col[i] != 0:
            if previous == None:
                previous = col[i]
            else:
                if previous == col[i]:
                    new_col[j] = 2 * col[i]
                    new_score = score + new_col[j]
                    j += 1
                    previous = None
                else:
                    new_col[j] = previous
                    j += 1
                    previous = col[i]
    if previous != None:
        new_col[j] = previous
    score = new_score
    return new_col

def check_game_over(board):
    checker = 0
    game_over = False
    for i in range(0,4):
        if (np.array_equal(board,move(board,i))):
            checker = (checker+1)
            if checker == 4:
                game_over = True
    return game_over

def main_loop(board, direction):
    new_board = move(board, direction)
    moved = False
    if (new_board == board).all():
        # move is invalid
        pass
    else:
        moved = True
        fill_cell(new_board)
    return (moved, new_board, score, check_game_over(board))
