import numpy as np
from numpy import zeros
import game_logic
import monte_carlo
import weighted_table

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
    monte_carlo.get_best_move(Game.board,5)
    '''
    while(game_logic.main_loop(Game.board,0)[3] == False):
        Game.board = game_logic.main_loop(Game.board,monte_carlo.alg(Game,1000,5))[1]
    print("stop: "+str(Game.score))
    print(Game.board)
    '''

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
