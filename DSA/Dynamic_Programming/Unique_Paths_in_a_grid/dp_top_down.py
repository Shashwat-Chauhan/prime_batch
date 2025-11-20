m = 10
n = 10

dp = [[-1] * n for _ in range(m)]


def find_paths(row , col):
    if row == 0 and col == 0:
        return 1

    if row < 0 or col < 0:
        return 0

    if dp[row][col] != -1:
        return dp[row][col]

    up = find_paths(row - 1 , col)
    left = find_paths(row , col - 1)

    dp[row][col] = up + left
    return dp[row][col]

ans = find_paths(m-1 , n-1)
print(ans)
