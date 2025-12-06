arr = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

def rev(l: int, r:int):
    if l >= r:
        return 
    
    arr[l] , arr[r] = arr[r] , arr[l]

    rev(l + 1 , r - 1)


rev(0 , len(arr) - 1)
print(arr)