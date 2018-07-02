import game_logic
weight_board = [[10,8,7,6.5],
                [0.5,0.7,1,3],
                [-.5,-1.5,-1.8,-2],
                [-3.8,-3.7,-3.5,-3]]

def getMove(board):  
    empty_cells = []
    for x in range(0,4):
            for y in range(0,4):
                if(board[x][y] == 0):
                    empty_cells.append(0)
    test_depth = len(empty_cells)
    depth_map = [5,4,4,3,3,2,2,2,2,2,2,2,2,2,2,2]
    depth = depth_map[test_depth]
    
    score = 0
    best_move = 0
    false_counter = 0
    for i in range(0, 4):       
        if(game_logic.main_loop(board,i)[0] == True):
            temp_board = game_logic.main_loop(board,i,0)[1]
            temp_score = getScore(temp_board, depth)
            if (temp_score > score):
                best_move = i
                score = temp_score
        else:
            false_counter += 1
            if(false_counter == 4):
                return -1
            
    return best_move

def getScore(board, depth):
    score = 0
    if (depth == 0):              
        for j in range(0, 4):
            for k in range(0, 4):
                score += weight_board[j][k] * board[j][k]
        return score
    
    empty_cells = []
    for x in range(0,4):
        for y in range(0,4):
            if(board[x][y] == 0):
                empty_cells.append(0)

    for i in range(0,len(empty_cells)+1):
        temp_board = game_logic.fill_cell(board,2)
        for i in range(0, 4):
            if(game_logic.main_loop(temp_board,i)[0] == True):
                temp_board = game_logic.main_loop(board,i,0)[1]
                score += getScore(temp_board, depth-1)
                
    if (len(empty_cells) > 0):
        score = score/len(empty_cells)
        score += len(empty_cells) * 10 
    return score
