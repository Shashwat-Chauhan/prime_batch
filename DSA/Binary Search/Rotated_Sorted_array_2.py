def search(low:int , high:int , target:int , arr:list[int]):
    while(low<=high):
        mid = (low+high)//2

        if arr[mid] == target:
            return mid

        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low+=1
            high-=1
            continue
        elif arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

arr = [3,3,1,2,3,3,3,3]
ans = search(0 , len(arr)-1 , 2 , arr)
print(ans)

