import game_logic
import weighted_table
import numpy as np
import sys
from numpy import array, zeros, rot90
from random import randint, random

def minimax(board,depth,agent, alpha, beta):
    best_score = 0
    best_move = -1
    #print(depth)
    if(depth == 0):
        #print(board)
        return (best_move,weighted_table.getScore(board,0,0))
    else:
        if(agent == "PLAYER"):
            #min
            best_score = -np.inf
            for i in range(0,4):
                if(game_logic.main_loop(board,i)[0] == False):
                    continue
                temp_board = game_logic.main_loop(board,i)[1]
                current_score = minimax(temp_board, depth-1, "COMPUTER", alpha, beta)[1]
                if(current_score > best_score):
                    alpha = max(alpha,best_score)
                    best_score = current_score
                    best_move = i
                if (beta <= alpha):
                    break
        elif(agent == "COMPUTER"):
            #max
            best_score = np.inf
            empty_cells = []
            for x in range(0,4):
                for y in range(0,4):
                    if(board[x][y] == 0):
                        empty_cells.append(0)

            if(len(empty_cells) == 0):
                best_score = 0
        
            for i in range(0,len(empty_cells)):
                temp_board = game_logic.fill_cell(board)
                current_score = minimax(temp_board, depth-1, "PLAYER", alpha, beta)[1]
                current_score += len(empty_cells)*10
                if(current_score < best_score):
                    beta = min(beta,best_score)
                    best_score = current_score
                if(beta <= alpha):
                    break
            
    #print(best_move)
    return (best_move,best_score)
