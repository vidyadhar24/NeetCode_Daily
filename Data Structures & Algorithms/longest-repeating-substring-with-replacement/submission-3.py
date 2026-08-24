class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        frq_map = {}
        l = 0
        res = 0

        # step one : update the char map
        for r in range(len(s)):
            frq_map[s[r]] = 1 + frq_map.get(s[r], 0)


            # Apply the key logic, check for the values to be replaced
            # if not shrink the window and update the freq map   
            # length of the window = (r - l + 1)
            while (r - l + 1) - max(frq_map.values()) > k:
                frq_map[s[l]] -= 1
                l += 1

            # At each increment, update the result
            res = max(res, (r - l + 1))

        return res



'''
s = "AAABABB", k = 1
ANSWER = AAABA -> where by changing B - A, (only one change is allowed K = 1), it becomes the longest one

Three steps

1. start from the left (l) and keep going to the right to create a window

2. While doing so.. add a character map of frequency.. like {A: 2, B: 4} etc.,
    - Now, the key here is the following formula
    - in the given window - (AAAB A:3 B:1), 
        - if the (length of the window - max of freqent char ) < k ie., 4 - 3  = 1 which is less that k
        - meaning there is scope for one item to change and K being 1 allows that
        - if this condition is met with, we can go ahead increase the window

3. if not, as in the above code, we shrink the window from the left and also update the freq map
        - at each increment of the window size, we keep tracking of the result, as max of current result or length
        - of the window
        - return the result at the end


'''
        