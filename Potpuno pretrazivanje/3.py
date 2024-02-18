from itertools import permutations

niz_stringova = input()

perms = set(permutations(niz_stringova))


for i in perms:
    print(i)

