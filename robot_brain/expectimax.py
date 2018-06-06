import game_logic
import weighted_table
import numpy as np

def get_best_move(board,depth):
    score = 0
    best_move = -1
    for i in range(0,4):
        temp_board = board
        print(temp_board)
        if(game_logic.main_loop(temp_board,i)[0] == False):
            continue
        print("LEGAL MOVE: "+str(i))
        temp_score = expectimax(temp_board,depth-1,"board")
        if(temp_score > score):
            best_move = i
            score = temp_score
    print("BEST MOVE: "+str(best_move))
    return best_move

def expectimax(board,depth,agent):
    if (depth == 0):
        return weighted_table.getScore(board,0,0)
    elif(agent == "player"):
        score = 0
        for i in range(0,4):
            temp_board = board
            temp_state = game_logic.main_loop(temp_board,i,0)
            temp_board = temp_state[1]
            next_level = temp_state[0]
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
                if(board[x][y] == 0):
                    empty_cells.append(0)
                    
        for i in range(0,len(empty_cells)):
            #4
            temp_board = board
            game_logic.fill_cell(temp_board,4)
            temp_score = expectimax(temp_board,depth-1,"player")
            if(temp_score == 0):
                score += 0
            else:
                score += (0.1*temp_score)
            #2
            temp_board = board
            game_logic.fill_cell(temp_board,2)
            temp_score = expectimax(temp_board,depth-1,"player")
            if(temp_score == 0):
                score += 0
            else:
                score += (0.9*temp_score)
        length = len(empty_cells)
        if (length == 0):
            length = 1
        score = score/length
        return score
            



