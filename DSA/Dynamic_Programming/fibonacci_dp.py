

def fib(dp: list , n: int):
    for i in range(2 , n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[-1]
n = 8
dp = [0]* (n+1)
dp[0] = 0
dp[1] = 1
ans = fib(dp , 8)

print(ans)