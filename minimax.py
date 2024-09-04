import math
from evaluate import evaluate
from moveleft import is_move_left
from printboard import printboard

def minimax(board, depth, maximizing_player, alpha, beta):

    score = evaluate(board)

    # Terminal states
    if score == 10:
        return score - depth  #* Quick wins
    elif score == -10:
        return score + depth  #* prevent losses
    
    if not is_move_left(board, 4) or depth == 7:  # Increased max depth
        return 0

    if maximizing_player:
        best = -math.inf
        for i in range(4):
            for j in range(4):
                if board[i][j] == '_':
                    board[i][j] = 'x'
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = '_'
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(4):
            for j in range(4):
                if board[i][j] == '_':
                    board[i][j] = 'o'
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = '_'
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best
