class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1   

        return True


    def alphaNum(self, c):
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')    
        )
    
    # Simple alternate solution

    class Solution:
        def isPalindrome(self, s: str) -> bool:
            #loop through all the characters and check if it is an isalnum, convert to lower
            #store the output, reverse the output and compare
            result = ""
            for c in s:
                if c.isalnum():
                    result += c.lower()
            return result == result[::-1]
