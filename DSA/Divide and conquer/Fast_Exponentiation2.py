def fast_expo(num , k):
    if k == 0:
        return 1

    x = fast_expo(num , k//3)
    if k %3 == 1:
        return x*x*x* num
    elif k%3 == 2:
        return x*x*x *num*num
    else:
        return x*x*x

print(fast_expo(3,7))


#This approach is not better than the previous approach where problem is subdivided into 2 parts for high values of K. This is because the average work done per function call is more in this case, which will add upto higher time complexity in the longer run.