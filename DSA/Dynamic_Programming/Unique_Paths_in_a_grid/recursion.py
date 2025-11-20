# You are given a (m x n) matrix , you are at the 0,0 index , find the number of paths to reach (m-1, n-1).

def find_paths(row , col):
    if row == 0 and col == 0:
        return 1

    if row < 0 or col < 0:
        return 0
    
    up = find_paths(row - 1 , col)
    left = find_paths(row , col - 1)

    return up + left

m = 10
n = 10
ans = find_paths(m - 1 , n - 1)
print(ans)