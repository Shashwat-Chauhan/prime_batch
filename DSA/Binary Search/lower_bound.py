def lower_bound(arr: list[int], low: int, high: int, bound: int):
    ans = high + 1  # Default to size of array (out of range)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= bound:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def upper_bound(arr: list[int], low: int, high: int, bound: int):
    ans = high + 1  # Default to size of array (out of range)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > bound:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

arr = [1, 3, 5, 10, 21]
n = len(arr)  # Correct the high index

result = lower_bound(arr, 0, n - 1, 10)
print("Lower Bound Index:", result)

result2 = upper_bound(arr, 0, n - 1, 10)
print("Upper Bound Index:", result2)
