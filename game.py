import game_logic
import ai

Game = game_logic.Board_game_2048()

def init_game():
    game_logic.fill_cell(Game.board)
    print Game.board

def move(direction):
    Game.board = game_logic.main_loop(Game.board,direction)[1]
    print Game.board

def random():
    ai.auto_random(Game.board,250)
