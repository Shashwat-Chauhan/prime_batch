# Given n , find the sum of first n numbers
# Parameterised way
def find_sum(i , sum):
    if i < 1:
        print(sum)
        return

    find_sum(i - 1, sum + i)

find_sum(10 , 0)




# Functional Way
def find_sum_2(i):
    if i == 0:
        return 0
    
    return i + find_sum_2(i - 1)

ans = find_sum_2(10)
print(ans)