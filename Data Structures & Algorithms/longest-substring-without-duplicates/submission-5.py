class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Input :  s = "abcabcbb"
        # Output: 3

        l = 0
        char_set = set()
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            res = max(res, r - l + 1)

        return res


    '''
    Use sliding window to solve this...

        s = "a   b   c   a   b   c   b   b"
        Idx: 0   1   2   3   4   5   6   7
        -----------------------------------
        r=0 [a]                             l=0, res=1
        r=1 [a   b]                         l=0, res=2
        r=2 [a   b   c]                     l=0, res=3
        r=3     [b   c   a]                 l=1, res=3 (l moves to drop 'a')
        r=4         [c   a   b]             l=2, res=3 (l moves to drop 'b')
        r=5             [a   b   c]         l=3, res=3 (l moves to drop 'c')
        r=6                     [c   b]     l=5, res=3 (l moves to drop 'a', 'b')
        r=7                          [b]    l=7, res=3 (l moves to drop 'c', 'b')

     1. Initate left pointer and right pointer
        - right pointer will be dynamic, it keeps chaging for each left point
     2. we will only loop through n times (for r in range(len(s)))..but at each step we check if the window has any dups
     3. Set data structure is used here as it is efficient for 'contains'..lookign for an item in the the list / set
     4. though it looks a bit complete, understand like this
        - loop through the list
        - add the right one to the set
        - But before that, check if the substring from the left to the right has any dups..
        - sometimes, the dups won't be at the start and end, but can be in the midle as well
        - that is why, we keep moving the left until substring has no dups (ref r=6 above)
        - at each step, we are overwriting the max length
        - finally, return the max length
    '''





