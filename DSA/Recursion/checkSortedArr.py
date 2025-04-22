def checkSorted(arr:list[int] , n:int)->bool:
    if n == 1:
        return True
    return arr[n-1] >= arr[n-2] and checkSorted(arr , n-1)

arr = [0,1,2,3,4,5]
print(checkSorted(arr,len(arr)))