import game_logic

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
                print("SCOOOOOREEE:"+str(score))
                #print board

#per temp_move een temp_board en elke move een paar keer doen (depth) en zien welke de hoogste score heeft, die move returnen
def alg(Game,depth):
    for x in range(0, depth):
        Temp_game = game_logic.Board_game_2048()
        Temp_game.board = Game.board
        best_move = False
        while(game_logic.main_loop(Temp_game.board,0)[3] == False):
            for i in range(0,4):
                if(game_logic.main_loop(Temp_game.board,i)[0] == True):
                    Temp_game.board = game_logic.main_loop(Temp_game.board,i)[1]
                    #print Temp_game.board
                    print Temp_game
    return best_move

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
