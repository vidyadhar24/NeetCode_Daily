class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        frq_map = {}
        l = 0
        res = 0

        for r in range(len(s)):
            frq_map[s[r]] = 1 + frq_map.get(s[r], 0)

            while (r - l + 1) - max(frq_map.values()) > k:
                frq_map[s[l]] -= 1
                l += 1


            res = max(res, (r - l + 1))

        return res
        