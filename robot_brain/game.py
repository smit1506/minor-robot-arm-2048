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
    while(not(game_over)):
        temp_board = []
        temp_board = Game.board
        best_move = minimax.minimax(temp_board,4,"PLAYER")[0]
        Game.board = game_logic.main_loop(temp_board,best_move)[1]
        print("New board with move: "+str(best_move))
        print(Game.board)
        if(game_logic.main_loop(Game.board,0)[3]):
            print("NOOOOO GAME OVAAAHHR")
            print(Game.board)
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
