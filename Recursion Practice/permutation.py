def permute(ds , arr , ans , freq):
    
    if len(ds) == len(arr):
        ans.append(ds.copy())
        return

    for i in range(len(arr)):
        if(not freq[i]):  
            ds.append(arr[i])
            freq[i] = 1
            permute(ds , arr , ans , freq)
            freq[i] = 0
            ds.pop()
        
arr = [1 , 2 , 3]
ans = []
freq = [0]*len(arr)
ds = []
permute(ds , arr , ans , freq)
print(ans )