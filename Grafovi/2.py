def najveca_povrsina_otoka(matrica):
    if not matrica or not matrica[0]:
        return 0

    redovi = len(matrica)
    stupci = len(matrica[0])

    def dfs(i, j):
        if i < 0 or i >= redovi or j < 0 or j >= stupci or matrica[i][j] == '0':
            return 0
        matrica[i][j] = '0'
        povrsina = 1
        povrsina += dfs(i+1, j)
        povrsina += dfs(i-1, j)
        povrsina += dfs(i, j+1)
        povrsina += dfs(i, j-1)
        return povrsina

    najveca_povrsina = 0

    for i in range(redovi):
        for j in range(stupci):
            if matrica[i][j] == '1':
                trenutna_povrsina = dfs(i, j)
                najveca_povrsina = max(najveca_povrsina, trenutna_povrsina)

    return najveca_povrsina

# Unos podataka
M, N = map(int, input().split())
matrica = [list(input().split()) for _ in range(M)]

# Poziv funkcije i ispis rezultata
rezultat = najveca_povrsina_otoka(matrica)
print(rezultat)