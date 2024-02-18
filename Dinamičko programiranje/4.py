kovanice = [int(x) for x in input().split(" ")]
svota = int(input())

def coin_change(kovanice, svota):
    dp = [float('inf') for _ in range(svota+1)]
    dp[0] = 0
    
    
    for i in range(len(dp)):
        for c in kovanice:
            if i-c >= 0:
                dp[i] = min(dp[i], dp[i-c]+1)
    return -1 if dp[-1] == float('inf') else dp[-1]

print(coin_change(kovanice, svota))