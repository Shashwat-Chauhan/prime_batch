# Given an array of integers , return all the possible permutations of the integers in the array

'''
# arr = [1,2,3]

ans = [
  [1, 2, 3],
  [1, 3, 2],
  [2, 1, 3],
  [2, 3, 1],
  [3, 1, 2],
  [3, 2, 1]
]
'''

def permutations(nums: list):
    res = []

    def backtrack(path, remaining):
        if not remaining:
            res.append(path[:])
            return
        
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]] , remaining[:i] + remaining[i+1:])
        
    backtrack([] , nums)
    return res

nums = [1,2,3]
ans = permutations(nums)
for i in ans:
    print(i)

        




