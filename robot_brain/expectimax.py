import game_logic
import weighted_table
import numpy as np

def get_best_move(board,depth):
    score = 0
    best_move = 0
    for i in range(0,4):
        temp_board = board
        if(game_logic.main_loop(temp_board,i)[0] == False):
            continue
        temp_score = expectimax(temp_board,depth-1,"board")
        if(temp_score > score):
            best_move = i
            score = temp_score
    return best_move

def expectimax(board,depth,agent):
    if (depth == 0):
        weighted_table.getScore(board,depth)
    elif(agent == "player"):
        score = 0
        for i in range(0,4):
            temp_board = board
            #next_level = 
        return score
