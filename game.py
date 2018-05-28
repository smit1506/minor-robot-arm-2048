import numpy as np
from numpy import zeros
import game_logic
import ai
import ai2
Game = game_logic.Board_game_2048()

def init_game():
    Game.board = zeros((4, 4), dtype=np.int)
    game_logic.score = 0
    game_logic.fill_cell(Game.board)
    print Game.board

def move(direction):
    Game.board = game_logic.main_loop(Game.board,direction)[1]
    print Game.board

def random():
    init_game()
    ai.auto_random(Game.board,250)

def smart_move():
    move = ai2.smart_boi(Game.board,5)
    Game.board = game_logic.main_loop(Game.board,move)[1]
    print Game.board

def auto_smart_move():
    for x in range(0, 1000):
        smart_move()
