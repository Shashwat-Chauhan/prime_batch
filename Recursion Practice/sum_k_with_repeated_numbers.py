def find_subsequence(arr , k):
    n = len(arr)
    res = []
    temp = []

    def backtrack(idx , curr_sum):
        if idx >= n:
            if curr_sum == k:
                res.append(temp.copy())
                
            return
        elif curr_sum > k:
            return
        
        temp.append(arr[idx])
        backtrack(idx, curr_sum + arr[idx])
        temp.pop()

        backtrack(idx + 1 , curr_sum)


    backtrack(0 , 0)
    return res

arr = [ 1  , 2 , 3 , 4]
print(find_subsequence(arr , 7))
        