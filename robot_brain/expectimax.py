import game_logic
import weighted_table
import numpy as np
import sys
from numpy import array, zeros, rot90
from random import randint, random

def get_best_move(alg_board):
    empty_cells = []
    for x in range(0,4):
            for y in range(0,4):
                if(alg_board[x][y] == 0):
                    empty_cells.append(0)
    test_depth = len(empty_cells)
    depth_map = [9,8,7,6,6,6,5,5,5,4,4,4,3,3,3,3]
    depth = depth_map[test_depth]
    
    score = 0
    best_move = -1
    for i in range(0,4):
        temp_board = []
        temp_board = array(alg_board)
        if(game_logic.main_loop(temp_board,i)[0] == False):
            continue
        else:
            print("LEGAL MOVE: "+str(i))
        top_score = expectimax(temp_board,depth-1,"board")
        print(top_score)
        if(top_score > score):
            best_move = i
            score = top_score
    return best_move

def expectimax(alg_board,depth,agent):
    #print(depth)
    if (depth == 0):
        return weighted_table.getScore(alg_board,0,0)
    elif(agent == "player"):
        score = 0
        for i in range(0,4):
            temp_board = []
            temp_board = array(alg_board)
            temp_state = game_logic.main_loop(temp_board,i)
            temp_board = temp_state[1]
            next_level = temp_state[0]
            #print(temp_board)
            if (next_level == False):
                continue
            new_score = expectimax(temp_board,depth-1,"board")
            if(new_score > score):
                score = new_score
        return score
    elif(agent == "board"):
        score = 0
        empty_cells = []
        for x in range(0,4):
            for y in range(0,4):
                if(alg_board[x][y] == 0):
                    empty_cells.append(0)
                    
        for i in range(0,len(empty_cells)):
            #4
            temp_board = []
            temp_board = array(alg_board)
            temp_board = game_logic.fill_cell(temp_board,4)
            
            temp_score = expectimax(temp_board,depth-1,"player")
            if(temp_score == 0):
                score += 0
            else:
                score += (0.1*temp_score)
            #2
            temp_board = []
            temp_board = array(alg_board)
            temp_board = game_logic.fill_cell(alg_board,2)
            temp_score = expectimax(temp_board,depth-1,"player")
            if(temp_score == 0):
                score += 0
            else:
                score += (0.9*temp_score)
                
        length = len(empty_cells)
        if (length == 0):
            length = 1
            
        score = score/length
        #print(score)
        return score
            



