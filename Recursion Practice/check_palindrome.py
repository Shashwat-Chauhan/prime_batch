arr = 'aaaabccbaaaa'
n = len(arr) - 1
def check_palindrome(i):
    if arr[i] != arr[n - i]:
        return False

    if i >= n/2:
        return True
    
    return check_palindrome(i + 1)


print(check_palindrome(0))