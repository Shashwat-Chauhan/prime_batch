m = 10
n = 10

dp = [[-1] * n for _ in range(m)]
dp[0][0] = 1

def find_paths(m , n):
    for row in range(m):
        for col in range(n):
            if row == 0 and col == 0:
                continue
            if row > 0:
                up = dp[row - 1][col]
            else:
                up = 0
            
            if col > 0:
                left = dp[row][col - 1]
            else:
                left = 0
                
            dp[row][col] = up + left 

find_paths(m , n)

print(dp[m-1][n-1])    