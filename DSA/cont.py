def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        count = [0] * 101
        for x in arr:
            count[x] += 1

        # find first integer that occurs less than twice
        a = 0
        while count[a] >= 2:
            a += 1

        # find first integer that does not occur
        b = 0
        while count[b] >= 1:
            b += 1

        print(a + b)

# Run the function
if __name__ == "__main__":
    solve()
