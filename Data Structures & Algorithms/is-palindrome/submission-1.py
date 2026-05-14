class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        '''
        Input: s = "Was it a car or a cat I saw?"

        Output: true

        '''

        '''

        Idea is to compare the first one with the last, second one with the second last ..

        only traversing through the half is enough, because the other half is already compared with by that time

        the same mid_idx(len/2) works for both even / odd

        [a,s,s,a]. -> 4 // 2 =  2 (idx)
        [a,s,a].   -> 3// 2 =   1

        for even, it will stop after comparing s vs s (idx 1)
        for odd, it won't consider s (stops at idx 0)


        '''
        cleaned_s = "".join(l.upper() for l in s if l.isalpha() or l.isnumeric())

        mid_idx = len(cleaned_s) // 2

        for i in range(mid_idx):
            if cleaned_s[i] != cleaned_s[len(cleaned_s) -i -1]:
                return False

        return True
        
