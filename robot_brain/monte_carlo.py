import game_logic

def auto_random(board,times):
    moves = 0
    score = 0
    stop = False
    for x in range(0, times):
        false_counter = 0
        for i in range(0, 4):
            print("ahh")
            if(game_logic.main_loop(board,i)[3] == True):
                print("game over, with "+str(moves)+" moves and "+str(score)+" score")
                print(board)
                return
            state = game_logic.main_loop(board,i)
            score = state[2]
            board = state[1]
            if(game_logic.main_loop(board,i)[0] == True):
                moves = (moves+1)
                print board

#per temp_move een temp_board en elke move een paar keer doen (depth) en zien welke de hoogste score heeft, die move returnen
def monte_carlo(state):
    for x in range(0, depth):
        temp_state = state
        #while(temp_state)
    
    

def auto_depth(board,depth):
    
    for x in range(0, depth):
        temp_board = board
        #while
        

    '''
    moves = 0
    score = 0
    false_counter = 0
    temp_board = None
    
    for i in range(0, 3):
        temp_board = board
        
        if(game_logic.main_loop(board,i)[0] == False):
            false_counter = (false_counter+1)
        if(false_counter == 3):
            print("game over, with "+str(moves)+" moves and "+str(score)+" score")
            print(board)
            return
        state = game_logic.main_loop(board,i)
        score = state[2]
        board = state[1]
        if(game_logic.main_loop(board,i)[0] == True):
            moves = (moves+1)
            #print board
    '''
    print("lol")
