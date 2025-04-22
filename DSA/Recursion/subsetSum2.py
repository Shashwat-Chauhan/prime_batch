def subs(arr: list[int] , idx: int, temp: list[int]):
    if idx == len(arr):
        print(temp)
        return
    
    temp.append(arr[idx])
    subs(arr , idx+ 1 , temp)
    temp.pop()
    idx+=1
    while idx < len(arr) and arr[idx] == arr[idx-1]:
        idx += 1
    subs(arr, idx , temp)
    



arr = [1,2,2]
temp = []
arr = sorted(arr)
subs(arr, 0, temp)
