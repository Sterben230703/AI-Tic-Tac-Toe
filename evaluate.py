
#*  evaluate matrix for 4*4 tic-tac-toe
def evaluate(mat):
    """
    Evaluate the matrix mat
    """
    for i in range(4):
        if mat[i][0] == mat[i][1] and mat[i][1] == mat[i][2] and mat[i][2] == mat[i][3]:
            if mat[i][0] == 'x':
                return 10
            elif mat[i][0] == 'o':
                return -10
            
    for i in range(4):
        if mat[0][i] == mat[1][i] and mat[1][i] == mat[2][i] and mat[2][i] == mat[3][i]:
            if mat[0][i] == 'x':
                return 10
            elif mat[0][i] == 'o':
                return -10
            
    if mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[2][2] == mat[3][3]:
        if mat[0][0] == 'x':
            return 10
        elif mat[0][0] == 'o':
            return -10
    
    if mat[0][3] == mat[1][2] and mat[1][2] == mat[2][1] and mat[2][1] == mat[3][0]:
        if mat[0][3] == 'x':
            return 10
        elif mat[0][3] == 'o':
            return -10
        
#* Diamond shapes
    diamond_shapes = [
        [(0,1), (1,0), (1,2), (2,1)],
        [(1,2), (2,1), (2,3), (3,2)],
        [(0,2), (1,1), (2,2), (1,3)],
        [(2,0), (1,1), (2,2), (3,1)]
    ]
    for shape in diamond_shapes:
        if mat[shape[0][0]][shape[0][1]] == mat[shape[1][0]][shape[1][1]] == \
            mat[shape[2][0]][shape[2][1]] == mat[shape[3][0]][shape[3][1]] != '_':
            return 10 if mat[shape[0][0]][shape[0][1]] == 'x' else -10
    
#* Square shapes
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i+1][j] == mat[i][j+1] == mat[i+1][j+1] != '_':
                return 10 if mat[i][j] == 'x' else -10
    
#* Check for draw
    if all(mat[i][j] != '_' for i in range(4) for j in range(4)):
        return 0
    
#* Game is ongoing
    return 0