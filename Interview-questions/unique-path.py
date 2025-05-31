
# unique paths in a grid

# unique paths = (m + n -2)!/(m-1)!(n-1)!

def uniquePath(m, n):
    dp = [1] * n
    
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
            
    return dp[-1]

print(uniquePath(3, 7)) # 28