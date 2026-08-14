class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = 'abcba'
        # s = 'abba'

        s = [ltr.lower() for ltr in s if ltr.isalnum()]
        
        if not s or len(s) == 1:
            return True

        l = 0
        r = len(s) - 1
        mid_pnt = len(s) // 2

        while l < mid_pnt:
            if s[l] != s[r]:

                return False
            else:
                l += 1
                r -= 1
        return True
