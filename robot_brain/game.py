import numpy as np
from numpy import zeros
import game_logic
import monte_carlo
import weighted_table
import minimax

Game = game_logic.Board_game_2048()

def init_game():
    Game.board = zeros((4, 4), dtype=np.int)
    Game.score = 0
    game_logic.fill_cell(Game.board)

def move(direction):
    Game.board = game_logic.main_loop(Game.board,direction)[1]
    print Game.board

def random():
    init_game()
    monte_carlo.auto_random(Game.board,250)

def auto_alg():
    init_game()
    best_move = -2
    game_over = False
    depth = 4
    Game.board = [[1024,512,256,16],
                 [0,0,16,32],
                 [0,2,2,4],
                 [0,0,0,2]]
    while(not(game_over)):
        temp_board = []
        temp_board = Game.board
        empty_cells = []
        false_counter = 0
        
        for x in range(0,4):
            for y in range(0,4):
                if(temp_board[x][y] == 0):
                    empty_cells.append(0)
        test_depth = len(empty_cells)
        depth_map = [9,9,8,8,8,8,8,6,6,5,5,5,5,4,4,4]
        depth = depth_map[test_depth]

        best_move = minimax.minimax(temp_board,depth,"PLAYER")[0]
        Game.board = game_logic.main_loop(temp_board,best_move)[1]
        print("New board with move: "+str(best_move))
        print(Game.board)
        for i in range(0,4):
            if(game_logic.main_loop(temp_board,i)[0] != True):
                false_counter += 1
                if(false_counter == 4):
                    print("NOOOOO GAME OVAAAHHR")
                    game_over = True
    
def smart_move():
    move = weighted_table.getMove(Game.board,4)
    if(move == -1):
        return -1
    #Game.board = game_logic.main_loop(Game.board,move)[1]
    state = game_logic.main_loop(Game.board,move)
    Game.board = state[1]
    Game.score = Game.score + state[2]
    print Game.board
        
def auto_smart_move():
    init_game()
    while smart_move() != -1:
        continue
    print Game.board
    print Game.score
    print("Game over!")
