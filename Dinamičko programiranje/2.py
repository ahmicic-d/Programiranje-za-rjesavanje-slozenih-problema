def fibb(n):
    mem = [0, 1]
    
    
    for i in range(2, n+1):
        mem.append(mem[i-1] + mem[i-2])
        
    return mem[-1]

print(fibb(10))