def minimum(arr:list[int]):
    low = 0
    high = len(arr)-1
    min_el = float("inf")
    while(low <= high):
        mid = (low + high)//2

        if arr[low] <= arr[mid]:
            min_el = min(arr[low] , min_el)
            low = mid + 1

        else:
            min_el = min(arr[mid] , min_el)
            high = mid - 1
    return min_el

arr = [4,5,6,7,1,2,3,4]
ans = minimum(arr)
print(ans)



            




        