#Leetcode 198 
arr = [2,7,9,3,1]
dp = [-1] * len(arr)
dp[0] = arr[0]

def rob(idx):
    if idx == 0:
        return arr[0]

    if idx < 0:
        return 0

    if dp[idx] != -1:
        return dp[idx]

    take = arr[idx] + rob(idx-2)
    
    not_take = 0 + rob(idx-1)

    dp[idx] = max(take , not_take)
    return dp[idx]

rob(len(arr) -1)
print(dp[-1])