cls_l = [[8, 9],
        [11, 13],
        [9, 10],
        [8, 14],
        [15, 17],
        [10, 12],
        [8, 10]
        ]

cls_l.sort(key = lambda x: (x[1], x[0]))

enroll = []
end = -1 

for cls in cls_l:
    if end <= cls[0]:
        end = cls[1]
        enroll.append(cls)
print(enroll)