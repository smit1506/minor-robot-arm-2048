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

def fill_cell(board,number=1):
    i, j = (board == 0).nonzero()
    if i.size != 0:
        rnd = randint(0, i.size - 1)
        if(number == 1):
            board[i[rnd], j[rnd]] = 2 * ((random() > .9) + 1)
        else:
            board[i[rnd], j[rnd]] = number
    return board 

def move(board, direction):
    # 0: left, 1: up, 2: right, 3: down
    rotated_board = rot90(board, direction)
    cols = [rotated_board[i, :] for i in range(4)]
    new_board = array([move_left(col) for col in cols])
    return rot90(new_board, -direction)

def move_left(col):
    new_col = zeros((4), dtype=col.dtype)
    j = 0
    global test
    previous = None
    for i in range(col.size):
        if col[i] != 0:
            if previous == None:
                previous = col[i]
            else:
                if previous == col[i]:
                    new_col[j] = 2 * col[i]
                    j += 1
                    previous = None
                else:
                    new_col[j] = previous
                    j += 1
                    previous = col[i]
    if previous != None:
        new_col[j] = previous

    return new_col

def check_game_over(board):
    checker = 0
    game_over = False
    for i in range(0,4):
        if (np.array_equal(board,move(board,i))):
            checker += 1
            if checker == 4:
                game_over = True
    return game_over

def get_score(old_board,new_board):
    old = []
    new = []
    for i in range(4):
        for j in range(4):
            if (old_board[i][j] > 0):
                old.append(old_board[i][j])
            if (new_board[i][j] > 0):
                new.append(new_board[i][j])
    old = sorted(old,reverse=True)
    new = sorted(new,reverse=True)
    diff = []
    if (np.array_equal(old,new) == False):
        offset_i = 0
        for i in range(len(new)):
            if (new[i] != old[i+offset_i]):
                if (old[i+offset_i] == old[i+offset_i+1]):
                    diff.append(new[i])
                    offset_i = offset_i-1
                offset_i = offset_i+1
    return sum(diff)

def main_loop(board, direction, number=1):
    new_board = move(board, direction)
    moved = False
    delta_score = 0
    if (new_board == board).all():
        # move is invalid
        pass
    else:
        moved = True
        delta_score = get_score(board,new_board)
        if(number == 1):
            new_board = fill_cell(new_board)
        elif(number == 2 or number == 4):
            new_board = fill_cell(new_board,number)
    return (moved, new_board, delta_score, check_game_over(new_board))














