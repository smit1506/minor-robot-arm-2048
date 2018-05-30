import game_logic

def getMove(board, depth=5):
    score = 0
    best_move = 0
    false_counter = 0
    weight_board = [[6, 5, 4, 3], [5, 4, 3, 2], [4, 3, 2, 1], [3, 2, 1, 0]]

    for i in range(0, 4):
        if(game_logic.main_loop(board,i)[0] == True):
            temp_board = game_logic.main_loop(board,i)[1]
            temp_score = 0
            for j in range(0, 3):
                for k in range(0, 3):
                    temp_score += weight_board[j][k] * temp_board[j][k]
            if (temp_score > score):
                best_move = i
                score = temp_score
        else:
            false_counter = (false_counter+1)
            if(false_counter == 3):
                return-1

    return best_move
