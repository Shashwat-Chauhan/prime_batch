arr = [30 , 10 , 60 , 10 , 60 , 50]

def frog_jump(arr):
    dp = [-1] * len(arr)
    dp[0] = 0
    for idx in range(1 , len(arr)):
        print(dp)
        first_step = dp[idx-1] + abs(arr[idx] - arr[idx-1])
        second_step = float('inf')
        if idx > 1:
            second_step = dp[idx - 2] + abs(arr[idx] - arr[idx - 2])

        dp[idx] = min(first_step, second_step)
    print(dp)
    return dp[-1]

print(frog_jump(arr))





