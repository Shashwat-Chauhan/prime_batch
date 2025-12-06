# Given n , print 1 to n , using recursion
def print_fun(i , n):
    if i > n:
        return
    
    print(i)
    print_fun(i + 1 , n)


print_fun(1 , 10)

