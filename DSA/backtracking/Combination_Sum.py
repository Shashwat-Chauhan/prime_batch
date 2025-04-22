# Given an array , return the subsequence (numbers) which sums to a particular target

def findSum(arr: list[int] , idx:int, target: int , temp , ans):
    if target == 0:
        ans.append(temp[:])
        return
    
    if idx == len(arr) or target < 0:
        return 
    
    temp.append(arr[idx])
    findSum(arr , idx+1 , target - arr[idx] , temp , ans)
    temp.pop()
    findSum(arr , idx+1 , target  , temp , ans)


arr = [2, 3, 5]
target = 8
ans = []

findSum(arr , 0 , target , [], ans)
print(ans)