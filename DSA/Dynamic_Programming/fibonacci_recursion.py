# Find the nth fibonacci number using DP

def fib(n:int , dp:list[int]):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]

    dp[n] = fib(n-1 , dp) + fib(n-2 , dp)
    return dp[n]

dp = [] # Maintain a array called dp , which contains the result of the previous values.
n = 8
for i in range(n+1):
    dp.append(-1)
ans = fib(n, dp)
print(ans)