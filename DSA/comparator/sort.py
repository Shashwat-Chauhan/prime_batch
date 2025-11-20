from functools import cmp_to_key
from collections import Counter

arr = [2, 1, 5, 9, 6, 11, 4, 8]

def cmp(a, b):
    if a % 2 == 0 and b % 2 != 0:
        return -1
    if a % 2 != 0 and b % 2 == 0:
        return 1

    # Both even: sort ascending
    if a % 2 == 0 and b % 2 == 0:
        return a - b

    # Both odd: sort descending
    return b - a

sorted_arr = sorted(arr, key=cmp_to_key(cmp))
print(sorted_arr)

i = [2, 1 , 5 ,7 , 3, 7, 4, 2 ]


sorted_arr_using_lambda = sorted(
    arr,
    key=lambda x: (arr.count(x))
)

print(sorted_arr_using_lambda)
