# Frog needs to go from 1st staircase to nth staircase , he can jump either 1 or 2 times , the energy used in the jump is height[i-1] - height[j-1] (in jumping from ith to jth stair) , calc the minimum energy it requires to reach the nth stair

arr = [30 , 10 , 60 , 10 , 60 , 50]
dp = [-1] * len(arr)

def frog_jump(idx):
    if idx == 0:
        return 0

    if dp[idx] != -1:
        return dp[idx]

    left = frog_jump(idx - 1) + abs(arr[idx] - arr[idx-1])
    right = float('inf')
    if idx > 1:
        right = frog_jump(idx - 2) + abs(arr[idx] - arr[idx-2])

    dp[idx] = min(left, right)
    return dp[idx]

print(frog_jump(5))

# This solution is Top-Down / memoization , now try doing bottom up dp , ie tabulation 
