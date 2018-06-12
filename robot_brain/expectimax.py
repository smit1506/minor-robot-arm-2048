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
    depth_map = [5,5,5,4,3,3,3,2,2,2,2,2,2,2,2,2]
    depth = depth_map[test_depth]
    #depth = 5
    
    score = 0
    best_move = -1
    for i in range(0,4):
        temp_board = []
        temp_board = array(alg_board)
        if(game_logic.main_loop(temp_board,i)[0] == False):
            print("NOT A LEGAL MOVE: "+str(i))
            continue
        else:
            temp_board = game_logic.main_loop(alg_board,i,0)[1]
            print("LEGAL MOVE: "+str(i))
            
        current_score = expectimax(temp_board,depth-1,"board")
        print("OH SHIE:"+str(current_score)+">"+str(score)+" for move: "+str(i))
        if(current_score > score):
            best_move = i
            score = current_score
    print("BEST MOVE: "+str(best_move)+" score: "+str(score))
    return best_move

def expectimax(alg_board,depth,agent):
    if (depth == 0):
        return weighted_table.getScore(alg_board,0,0)
    elif(agent == "player"):
        score = 0
        for i in range(0,4):
            if(game_logic.main_loop(alg_board,i)[0] == False):
                continue
            new_board = game_logic.main_loop(alg_board,i,0)[1]
            current_score = expectimax(new_board,depth-1,"board")
            if(current_score > score):
                score = current_score
        return score
    elif(agent == "board"):
        score = 0
        empty_cells = []
        for x in range(0,4):
            for y in range(0,4):
                if(alg_board[x][y] == 0):
                    empty_cells.append(0)
            
        for i in range(0,len(empty_cells)+1):
            #4
            temp_board = array(alg_board)
            temp_board = game_logic.fill_cell(temp_board,4)
            temp_score = expectimax(temp_board,depth-1,"player")
            score += (0.1*temp_score)
            #2
            temp_board = array(alg_board)
            temp_board = game_logic.fill_cell(temp_board,2)
            temp_score = expectimax(temp_board,depth-1,"player")
            score += (0.9*temp_score)

        if (len(empty_cells) > 0):
            score = score/len(empty_cells)

        return score
            



