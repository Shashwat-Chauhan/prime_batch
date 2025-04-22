def fast_expo(num: int , k:int):
    if k == 0:
        return 1
    
    x = fast_expo(num , k//2)
    if k % 2 == 0:
        return x * x
    else:
        return x * x * num
print(fast_expo(2, 11))

#This is how funciton like pow() in c++ are implemented, their time complexities are log2(k)