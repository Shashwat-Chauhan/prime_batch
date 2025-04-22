class Solution:
    def partition(self, s: str) -> list[list[str]]:

        def check_palindrome(substr:str):
            return substr == substr[::-1]
        
        def palindrome(start: int, ans):
            if start == len(s):
                result.append(ans[:])
                return
            for end in range(start+1, len(s)+1):
                if check_palindrome(s[start:end]):
                    ans.append(s[start:end])
                    palindrome(end, ans)
                    ans.pop()    
    


        result = []
        palindrome(0 , [])
        return result 
a