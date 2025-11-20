def fibonacci(num , mp = None):

    if mp is None:
        mp = {}

    if num in mp:
        mp[num]

    if num <= 1:
        result = num

    else:
        result = fibonacci(num - 1) + fibonacci(num - 2)
    
    mp[num] = result
    return result
    
    # TC = O(n)
mp = {}
ans = fibonacci(20 , mp)
print(ans)