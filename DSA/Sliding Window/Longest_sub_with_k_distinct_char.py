# Q) Given a string , find the longest substring with atmost k distict characters

def solve(s: str, k: int) -> int:
    l = 0
    mp = {}
    ans = 0

    for r in range(len(s)):
        mp[s[r]] = mp.get(s[r], 0) + 1

        # Shrink window if more than k distinct
        while len(mp) > k:
            mp[s[l]] -= 1
            if mp[s[l]] == 0:
                del mp[s[l]]
            l += 1

        # Update answer (window size = r-l+1)
        ans = max(ans, r - l + 1)

    return ans

s = "aaabbccd"
k = 2
ans = solve(s , 2)
print(ans)


