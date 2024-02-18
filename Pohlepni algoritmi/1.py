n = int(input())

def kovano(n):
    kovanice = [1, 2, 5, 10, 20, 50, 100, 200]
    najveca = 0
    
    for c in kovanice:
        if c <= n:
            najveca = c
    return najveca



while True:
    v = kovano(n)
    
    if not v:
        break
    else:
        print(v, end=" ")
        n -= v