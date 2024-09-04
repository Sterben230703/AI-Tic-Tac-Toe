import math
# from evaluate import evaluate
from moveleft import is_move_left
from minimax import minimax

def findbestmove(board, player, n):
    
    best_score = -math.inf if player == 'x' else math.inf
    best_move = (-1, -1)
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == '_':
                board[i][j] = player
                if player == 'x':
                    score = minimax(board, 0, False, -math.inf, math.inf)
                else:
                    score = minimax(board, 0, True, -math.inf, math.inf)
                board[i][j] = '_'
                
                if (player == 'x' and score > best_score) or (player == 'o' and score < best_score):
                    best_score = score
                    best_move = (i, j)
    
    return best_move



    
board=[['o','o','x','o'],
       ['_','_','_','x'],
       ['_','_','x','_'],
       ['_','_','_','_']]

bestmove=findbestmove(board,'o',4)
print("The Optimal Move is :")
print("ROW:",bestmove[0]," COL:",bestmove[1])

# board=[['x','o','o','x'],
#        ['o','x','o','x'],
#        ['o','x','x','o'],
#        ['x','o','_','x']]