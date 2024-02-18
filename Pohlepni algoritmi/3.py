cls_l = [[8, 9],
        [11, 13],
        [9, 10],
        [8, 14],
        [15, 17],
        [10, 12],
        [8, 10]
        ]
cls_l.sort(key = lambda x: (x[1], x[0]))


predmeti = []
kraj = -1

for p in cls_l:
    if kraj <= p[0]:
        kraj = p[1]
        predmeti.append(p)

print(predmeti)