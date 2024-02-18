def solve(matrica):
    if not matrica or not matrica[0]:
        return
    
    retci = len(matrica)
    stupci = len(matrica[0])

    def dfs(i, j):
        if 0 <= i < retci and 0 <= j < stupci and matrica[i][j] == 'O':
            matrica[i][j] = 'D'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
    for i in range(retci):
        dfs(i, 0)
        dfs(i, stupci - 1)

    for j in range(stupci):
        dfs(0, j)
        dfs(retci - 1, j)

    for i in range(retci):
        for j in range(stupci):
            if matrica[i][j] == 'O':
                matrica[i][j] = 'X'
            elif matrica[i][j] == 'D':
                matrica[i][j] = 'O'

matrica = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]

solve(matrica)

# Ispis rezultata
for redak in matrica:
    print(" ".join(redak))
