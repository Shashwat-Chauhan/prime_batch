class Solution:
    def subsetSums(self, arr):
        res = []
		temp = []
		n = len(arr)
        def backtrack(idx:int , curr_sum):
            if idx >= n:
                res.append(curr_sum)
                return
		    
		    backtrack(idx + 1 , curr_sum + arr[idx])

		    backtrack(idx + 1, curr_sum)
		   
		  
		backtrack(0 , 0)
		return res
		    
