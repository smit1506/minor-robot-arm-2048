import game_logic
weight_board = [[10,8,7,6.5],
                [0.5,0.7,1,3],
                [-.5,-1.5,-1.8,-2],
                [-3.8,-3.7,-3.5,-3]]

def getMove(board, depth):
    score = 0
    best_move = 0
    false_counter = 0

    empty_cells = []
    for x in range(0,4):
            for y in range(0,4):
                if(board[x][y] == 0):
                    empty_cells.append(0)
    test_depth = len(empty_cells)
    depth_map = [6,5,5,5,4,4,4,4,4,4,3,3,3,3,3,3]
    depth = depth_map[test_depth]

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
