from typing import List
#Approach2
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # Step 1: Precompute the palindrome matrix
        is_palindrome = [[False] * n for _ in range(n)]
        
        for length in range(n):  # length of substring
            for i in range(n - length):
                j = i + length
                if s[i] == s[j]:  # Check first and last character
                    if length <= 1:  # Single char or two same chars (aa)
                        is_palindrome[i][j] = True
                    else:  # Check inside the substring
                        is_palindrome[i][j] = is_palindrome[i + 1][j - 1]
        
        # Step 2: Backtracking with DP table lookup
        def backtrack(start: int, path: List[str]):
            if start == n:
                result.append(path[:])  # Append a copy of path
                return
            
            for end in range(start, n):
                if is_palindrome[start][end]:  # Use precomputed table
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()  # Backtrack
        
        result = []
        backtrack(0, [])
        return result
