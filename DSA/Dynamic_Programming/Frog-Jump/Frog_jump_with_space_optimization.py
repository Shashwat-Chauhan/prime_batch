arr = [30 , 10 , 60 , 10 , 60 , 50]

def frog_jump(arr):
    prev = 0
    prev2 = 0

    for idx in range(1 , len(arr)):
        first_step = prev + abs(arr[idx] - arr[idx-1])
        second_step = float('inf')
        if idx > 1:
            second_step = prev2 + abs(arr[idx] - arr[idx - 2])

        curr = min(first_step, second_step)
        prev2 = prev
        prev = curr
    return prev

print(frog_jump(arr))


