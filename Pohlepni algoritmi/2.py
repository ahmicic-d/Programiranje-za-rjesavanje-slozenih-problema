rijec_lista=[str(x) for x in input().split(" ")]
rez=[]
for i in rijec_lista:
    if i =='A':
        rez.append('00')
    if i =='B':
        rez.append('01')
    if i =='C':
        rez.append('10')
    if i =='D':
        rez.append('11')
print(rez)