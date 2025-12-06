arr = [1 , 2 , 3]
temp = []
ans = []

def subsequence(idx , n):
    if idx >= n:
        ans.append(temp.copy())
        # print(temp)
        return
    temp.append(arr[idx])
    subsequence(idx + 1 , n)    
    temp.pop()
    subsequence(idx + 1 , n)

subsequence(0 , 3)
print(ans)