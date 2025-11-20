from functools import cmp_to_key
def sortKey(a , b):
    if a < b:
        return -1
    elif a > b :
        return 1
    else:
        return 0
    

arr = [2,3,7,4,2,8,4,2,5,1]
sorted_arr = sorted(arr , key= cmp_to_key(sortKey))
print(sorted_arr)

arr_2 = [1,4,2,5,7,4,2,4,67,4,3,1]
sorted_arr_2 = sorted(arr_2 , key = lambda x : x)
print(sorted_arr_2)

