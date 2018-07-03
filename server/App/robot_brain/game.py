from timeit import default_timer as timer
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
    
    start_timer = 0
    end_timer = 0
    timer_array = []
    times_2048 = 0
    
    while(not(game_over)):
        start_timer = timer()
        
        temp_board = []
        temp_board = Game.board
        empty_cells = []
        false_counter = 0
        
        for x in range(0,4):
            for y in range(0,4):
                if(temp_board[x][y] == 0):
                    empty_cells.append(0)
        test_depth = len(empty_cells)
        depth_map = [9,9,8,7,7,7,7,6,6,6,6,6,5,4,4,4]
        depth = depth_map[test_depth]

        best_move = minimax.minimax(temp_board,depth,"PLAYER", -np.inf,np.inf)[0]
        Game.board = game_logic.main_loop(temp_board,best_move)[1]
        
        print("New board with move: "+str(best_move))
        print(Game.board)
        for i in range(0,4):
            if(game_logic.main_loop(temp_board,i)[0] != True):
                false_counter += 1
                if(false_counter == 4):
                    print("NOOOOO GAME OVAAAHHR")
                    game_over = True
                    
        end_timer = timer()
        print("TIME ELAPSED THIS MOVE:")
        print(end_timer-start_timer)
        print("-")
        timer_array.append(end_timer-start_timer)
        
    print("TOTAL TIME ELAPSED:")
    print(sum(timer_array))
    print("AVERAGE TIME EACH MOVE:")
    print(np.mean(timer_array))

    for x in range(0,4):
            for y in range(0,4):
                if(Game.board[x][y] >= 2048):
                   times_2048 += 1
    return np.mean(timer_array),sum(timer_array),times_2048

def auto_alg_research():
    average_time_per_move = []
    average_time_per_game_over = []
    times_2048 = 0
    
    for i in range(0,10):
        result_set = auto_alg()
        average_time_per_move.append(result_set[0])
        average_time_per_game_over.append(result_set[1])
        times_2048 += result_set[2]

    print("/n -----------------------------------------------------")

    print("AVERAGE TIME PER MOVE:")
    print(np.mean(average_time_per_move))
    
    print("AVERAGE COMPLETION TIME EACH GAME:")
    print(np.mean(average_time_per_game_over))
    
    print("TIMES 2048 OUT OF 10 GAMES:")
    print(times_2048)

def smart_move_research():
    result_set = []
    average_time_per_move = []
    average_time_per_game_over = []
    times_2048 = 0
    
    for i in range(0,2):
        result_set = auto_smart_move()
        average_time_per_move.append(result_set[0])
        average_time_per_game_over.append(result_set[1])
        times_2048 += result_set[2]

    print("/n -----------------------------------------------------")

    print("AVERAGE TIME PER MOVE:")
    print(np.mean(average_time_per_move))
    
    print("AVERAGE COMPLETION TIME EACH GAME:")
    print(np.mean(average_time_per_game_over))
    
    print("TIMES 2048 OUT OF 10 GAMES:")
    print(times_2048)


def auto_smart_move():
    timer_array = []
    times_2048 = 0
    game_over = False
    
    init_game()

    while(game_over == False):
        start_timer = 0
        end_timer = 0

        start_timer = timer()
        
        move = weighted_table.getMove(Game.board,4)
        if(move == -1):
            break
        state = game_logic.main_loop(Game.board,move)
        Game.board = state[1]
        Game.score = Game.score + state[2]
        print Game.board
        
        end_timer = timer()
        
        print("TIME ELAPSED THIS MOVE:")
        print(end_timer-start_timer)
        print("-")
        
        timer_array.append(end_timer-start_timer)
    
    print Game.board
    print Game.score
    print("Game over!")

    for x in range(0,4):
        for y in range(0,4):
            if(Game.board[x][y] >= 2048):
                times_2048 += 1 
    
    return np.mean(timer_array),sum(timer_array),times_2048
