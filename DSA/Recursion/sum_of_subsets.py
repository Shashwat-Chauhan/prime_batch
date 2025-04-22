
count = 0
def SUM(arr: list[int] , idx: int, curr_sum: int):
    global count
    if idx == len(arr):
        if curr_sum == 0:
            count+=1
            return 
        else:
            return 
    
    SUM(arr, idx+1 , curr_sum - arr[idx])
    SUM(arr, idx+1, curr_sum)

arr = [1, 2, 3]
targetSum = 3 
curr_sum = 0

SUM(arr, 0, targetSum)
print(count)