import game_logic
import numpy as np

def auto_random(board,times):
    moves = 0
    score = 0
    stop = False
    for x in range(0, times):
        false_counter = 0
        for i in range(0, 4):
            if(game_logic.main_loop(board,i)[3] == True):
                print("game over, with "+str(moves)+" moves and "+str(score)+" score")
                print(board)
                return
            state = game_logic.main_loop(board,i)
            score = score + state[2]
            board = state[1]
            if(game_logic.main_loop(board,i)[0] == True):
                moves = (moves+1)

def alg(Game,max_depth):
    best_move = 0
    best_avg_score = 0
    score_to_add = 0
    for i in range(0,4):
        Temp_game = game_logic.Board_game_2048()
        Temp_game.board = Game.board
        temp_score = 0
        temp_avg_score = []
        if(game_logic.main_loop(Temp_game.board,i)[0] == False):
            continue
        for depth in range(0,max_depth):
            while(game_logic.main_loop(Temp_game.board,0)[3] == False):
                for j in range(0,4):
                    temp_game_state = game_logic.main_loop(Temp_game.board,j)
                    Temp_game.board = temp_game_state[1]
                    temp_score += temp_game_state[2]
                if(game_logic.main_loop(Temp_game.board,0)[3] == True):
                    temp_avg_score.append(temp_score)
                    Temp_game.board = Game.board
                    break
            if(np.mean(temp_avg_score) > best_avg_score):
                best_avg_score = temp_score
                best_move = i
                temp_score = 0
    print("Best move: "+str(best_move)+" with score: "+str(best_avg_score))
    print(Game.board)
    return best_move
