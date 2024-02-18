from collections import defaultdict

def bojanje_grafa(n, prijateljstva):
    graf = defaultdict(list)
    for prijateljstvo in prijateljstva:
        a, b = prijateljstvo
        graf[a].append(b)
        graf[b].append(a)

    boje = [-1] * (n + 1)

    def bojanje_dfs(ucenik, boja):
        boje[ucenik] = boja
        for susjed in graf[ucenik]:
            if boje[susjed] == -1:
                if not bojanje_dfs(susjed, 1 - boja):
                    return False
            elif boje[susjed] == boja:
                return False
        return True

    for i in range(1, n + 1):
        if boje[i] == -1:
            if not bojanje_dfs(i, 0):
                return "NEMA"

    timovi = [1 if boja == 0 else 2 for boja in boje[1:]]
    return timovi

n, m = map(int, input().split())
prijateljstva = [tuple(map(int, input().split())) for _ in range(m)]

rezultat = bojanje_grafa(n, prijateljstva)

if rezultat == "NEMA":
    print("NEMA")
else:
    print(" ".join(map(str, rezultat)))



