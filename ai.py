import game_logic

def auto_random(board,times):
    moves = 0
    stop = False
    for x in range(0, times):
        false_counter = 0
        for i in range(0, 3):
            if(game_logic.main_loop(board,i)[0] == False):
                false_counter = (false_counter+1)
            if(false_counter == 3):
                print("game over, with "+str(moves)+" moves")
                print(board)
                return
            board = game_logic.main_loop(board,i)[1]
            if(game_logic.main_loop(board,i)[0] == True):
                moves = (moves+1)
                #print board

