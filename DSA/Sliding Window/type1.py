# Type 1
# This type of questions have a constant window 

arr = [-1 , 2 , 3 , 3 , 4 , 5 , -1, -3]
k = 4

# Find longest subarray of length k 

l = 0
r = k - 1
max_sum = sum(arr[:r+1])
summ = max_sum
while(r < len(arr) - 1):
    summ -= arr[l]
    l += 1
    r += 1
    summ += arr[r]
    max_sum = max(max_sum , summ)

print(max_sum)

