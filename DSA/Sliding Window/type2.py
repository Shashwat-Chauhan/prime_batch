# Type 2
# This type of questions are as follows 
# Longest subarray/ substring where <condition>


arr = [-1 , 2 , 3 , 3 , 4 , 5 , -1, -3]
k = 4

# Find Longest subarray with sum <= k

l = 0
r = 0
summ = 0
max_len = 0
while(r < len(arr)):
    summ += arr[r]
    if (summ > k):
        summ -= arr[l]
        l += 1

    if summ <= k:
        max_len = max(max_len, r - l + 1)
    
    r += 1

print(max_len)