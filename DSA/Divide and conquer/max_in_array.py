def max_in_array(arr: list[int], i:int , j: int):

    if i == j:
        return arr[i]
    
    mid = (i + j) // 2
    left = max_in_array(arr , i, mid)
    right = max_in_array(arr , mid + 1, j)

    return max(left , right)

arr = [7,1,4,3,2,6,5]
ans = max_in_array(arr , 0 , 7)
print(ans)
