"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
ALPHA =  -math.inf
BETA = math.inf
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    # """
    vals = sum([1 for row in board for x in row if x != EMPTY])
    player = X if vals % 2 == 0 else O
    return player




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = [(i,j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]
    
    return moves



def result(board, action):

    """
    Returns the board that results from making move (i, j) on the board.
    """
    p = player(board) 
    i,j = action
    if board[i][j] != EMPTY:
        print('board',board)
        print('action',action)
        board[i][i] == p
        print('board',board)
        raise Exception('Not a playable move')
    else:
        board[i][j] = p
    return board




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    first_row  = board[0][:]
    second_row = board[1][:]
    third_row  = board[2][:]

    first_col  = [col[0] for col in board]
    second_col = [col[1] for col in board]
    third_col  = [col[2] for col in board]

    diag_1 = [board[i][i] for i in range(3)]
    diag_2 = [board[2-i][2-1] for i in range(3)]

    data = [first_row,second_row,third_row, first_col,second_col,third_col,diag_1,diag_2]
    for d in data:
        if all([x == 'X' for x in d]):
            return 'X'
        elif all([x == 'O' for x in d]):
            return  'O'

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or [item for row in board for item in row].count(EMPTY) == 0:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == 'X':
        return 1
    elif win == '0':
        return -1
    else:
        return 0

def evaluate_utility(row,value=0.45) -> float:
    score = 0
    if (row[0] and row[1] == 'X' and row[2] == EMPTY)  or ( row[1] and row[2] == 'X' and row[0] == EMPTY) or ( row[0] and row[2] == 'X' and row[1] == EMPTY):
        score += value
    elif ( row[0] and row[1] == 'O' and row[2] == EMPTY) or ( row[1] and row[2] == 'O' and row[0] == EMPTY) or ( row[0] and row[2] == 'O' and row[1] == EMPTY):
        score -= value
    return score
    

def evaluate_utility_board(board):
    score = 0
    first_row  = board[0][:]
    second_row = board[1][:]
    third_row  = board[2][:]

    first_col  = [col[0] for col in board]
    second_col = [col[1] for col in board]
    third_col  = [col[2] for col in board]

    diag_1 = [board[i][i] for i in range(3)]
    diag_2 = [board[2-i][2-1] for i in range(3)]

    
    data = [first_row,second_row,third_row, first_col,second_col,third_col,diag_1,diag_2]
    score = 0
    for d in data:
        score += evaluate_utility(row = d)

    return score


def minimax(board):

    p = player(board)
    if p == 'X':
        best = [(-1,-1),-math.inf]
    if p == 'O':
        best = [(-1,-1),math.inf]


    if terminal(board):
        score = utility(board)
        return [(-1,-1),score]

    for move in actions(board):
        state = 0
        board = result(board,move)
        score = minimax(board)
        state +=1
        i,j = move
        board[i][j] = EMPTY
        score[0] = (i,j)

        if p == 'X':
            if score[1] > best[1]:
                best = score
                
        else:
            if score[1] < best[1]:
                best = score

    return best


# def minimax_alpha_beta(board,alpha=ALPHA,beta = BETA):
def minimax_alpha_beta(board):
    p = player(board)
    global ALPHA
    global BETA
    if p == 'X':
        best = [(-1,-1),-math.inf]
    if p == 'O':
        best = [(-1,-1),math.inf]


    if terminal(board):
        score = utility(board)
        return [(-1,-1),score]

    for move in actions(board):
        print('ALPHA',ALPHA)
        state = 0
        board = result(board,move)
        score = minimax_alpha_beta(board)
        state +=1
        i,j = move
        board[i][j] = EMPTY
        score[0] = (i,j)

        if p == 'X':
            if score[1] > best[1]:
                best = score
            
            if best[1] >= BETA:
                return score
            if best[1] > ALPHA:
                ALPHA = best[1]
                
        else:
            if score[1] < best[1]:
                best = score

            if best[1] <= ALPHA:
                return score
            
            if best[1] < BETA:
                BETA = best[1]

    return best











    
