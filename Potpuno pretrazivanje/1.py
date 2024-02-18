niz = []

def search(k, n, subset):
    
    if n == k:
        print(subset)
        
    else:
        search(k+1, n, subset)
        subset.append(k)
        search(k+1, n, subset)
        subset.pop()
        
n = 3

search(0, n, niz)
        