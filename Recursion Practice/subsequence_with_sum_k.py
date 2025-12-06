arr = [1 , 2, 4 , 5 , 6 , 3 , 1]

def find_sub_with_sum_k(arr , k):
    res = []
    temp = []

    def backtrack(idx , curr_sum):
        if idx >= len(arr):
            if curr_sum == k:
                res.append(temp.copy())
            return
        
        temp.append(arr[idx])
        backtrack(idx + 1 , curr_sum + arr[idx])

        temp.pop()
        backtrack(idx + 1 , curr_sum)
    
    backtrack(0 , 0)
    return res

ans = find_sub_with_sum_k(arr , 7)
print(ans)