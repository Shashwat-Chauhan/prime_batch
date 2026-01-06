def climbstairs(n):
    if n == 2:
        return 2
    
    if n == 1:
        return 1
    return climbstairs(n-1) + climbstairs(n-2)

n = 9
ans = climbstairs(n)
print(ans)


def climbstairs_using_bottom_up(n):
    dp = [0]* (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[-1]
        
ans2 = climbstairs_using_bottom_up(9)
print(ans2)
