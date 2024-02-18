def broj_otoka(matrica):
    if not matrica or not matrica[0]:
        return 0
    
    br_otoka = 0
    redovi = len(matrica)
    stupci = len(matrica[0])
    
    def dfs(i, j):
        if i < 0 or i >= redovi or j < 0 or j >= stupci or matrica[i][j] == '0':
            return
        matrica[i][j] = '0'
        
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
        
    for red in range(redovi):
        for stupac in range(stupci):
            if matrica[red][stupac] == '1':
                br_otoka += 1
                dfs(red, stupac)
        
    return br_otoka
    

M, N = map(int, input().split())

matrica = [list(input().split()) for _ in range(M)]

print(broj_otoka(matrica))



