# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]




def combination_sum_two(arr: list[int], target: int) -> list[list[int]]:
    res = []
    temp = []
    arr = sorted(arr)
    n = len(arr)

    def backtrack(idx: int , curr_sum: int):
        if idx >= n:
            if curr_sum == target:
                res.append(temp[:])
            return
        
        if curr_sum > target:
            return
        
        temp.append(arr[idx])
        backtrack(idx + 1 , curr_sum + arr[idx])
        temp.pop()

        idx += 1
        while(idx < n and arr[idx] == arr[idx-1]):
            idx += 1
        
        backtrack(idx , curr_sum)
    
    backtrack(0 , 0)
    return res

arr = [10,1,2,7,6,1,5]
target = 8
ans = combination_sum_two(arr , target)
print(ans)