def subsets(arr: list[int], idx: int, temp: list[int] , N):
    if idx == N:
        print(temp)
        return
    
    temp.append(arr[idx])
    subsets(arr, idx+1 , temp, N)
    temp.pop()

    subsets(arr, idx+1 , temp, N)

arr = [1,2,3]
temp = []
subsets(arr, 0 , temp , len(arr))
