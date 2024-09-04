def is_move_left(board,n):
    for i in range(n):
        for j in range(n):
            if board[i][j]=='_':
                return True
    return False