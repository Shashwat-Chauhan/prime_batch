# Now the frog can jump upto k steps at a time ie. 1 or 2 or 3 or 4 or 5 .......k
# Now determine the minimum jump he will reqquire if he can jump k steps at a time  
arr = [30 , 10 , 60 , 10 , 60 , 50]

def frog_jump(arr , k:int):
    dp = [float('inf')] * len(arr)
    dp[0] = 0

    for idx in range(1 , len(arr)):
        for j in range(1, k + 1):
            step = float('inf')
            if idx - j >= 0:
                cost = dp[idx - j] + abs(arr[idx] - arr[idx - j])
                dp[idx] = min(dp[idx] , cost)
    
    return dp[-1]

print(frog_jump(arr, 5))
        




        
