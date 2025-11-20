# Frog needs to go from 1st staircase to nth staircase , he can jump either 1 or 2 times , the energy used in the jump is height[i-1] - height[j-1] (in jumping from ith to jth stair) , calc the minimum energy it requires to reach the nth stair

arr = [30, 10 , 60 , 10 , 60 , 50]
def frogJump(idx):
    if idx == 0:
        return 0
    
    left = frogJump(idx - 1) + abs(arr[idx] - arr[idx-1])
    right = float("inf")

    if idx > 1:  
        right = frogJump(idx-2) + abs(arr[idx] - arr[idx-2])
 
    return min(left , right)

print(frogJump(5))

#Now try to cinvert this code into dp 