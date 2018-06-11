import game_logic
weight_board = [[6, 5, 4, 3],
                [5, 4, 3, 2],
                [4, 3, 2, 1],
                [3, 2, 1, 0]]

def getMove(board, depth):
    score = 0
    best_move = 0
    false_counter = 0
    for i in range(0, 4):       
        if(game_logic.main_loop(board,i)[0] == True):
            temp_board = game_logic.main_loop(board,i)[1]
            temp_score = getScore(temp_board, depth, 0)
            if (temp_score > score):
                best_move = i
                score = temp_score
        else:
            false_counter += 1
            if(false_counter == 4):
                return -1
            
    return best_move

def getScore(board, depth, score):
    if (depth == 0):
        score = 0
        for j in range(0, 4):
            for k in range(0, 4):
                score += weight_board[j][k] * board[j][k]
        return score
    
    for i in range(0, 4):
        if(game_logic.main_loop(board,i)[0] == True):
            temp_board = game_logic.main_loop(board,i)[1]
            temp_score = getScore(temp_board, depth-1, score)
            if (temp_score > score):
                score = temp_score
    return score
