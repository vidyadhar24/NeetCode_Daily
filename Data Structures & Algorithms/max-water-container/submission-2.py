class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l_p = 0
        r_p = len(heights) - 1
        max_wat = 0

        while l_p < r_p:
            area = (r_p - l_p) * min(heights[l_p], heights[r_p])
            max_wat = max(max_wat, area)

            if heights[l_p] < heights[r_p]:
                l_p += 1
            else:
                r_p -= 1

            
        return max_wat