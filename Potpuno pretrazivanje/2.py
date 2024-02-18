def ksum(k, l, n):

    bins = [format(i, "b").zfill(n) for i in range(2**n)]

    for sel in bins:
        total = 0
        
        for i, b in enumerate(sel):
            if b=="1":
                total+=l[i]

        if total == k:
            for i, b in enumerate(sel):
                if b=="1":
                    print(l[i])

lista = [1, 2, 3]
ksum(5, lista, 3)
