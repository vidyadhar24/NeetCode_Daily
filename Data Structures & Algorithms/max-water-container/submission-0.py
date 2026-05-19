class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left_pnt = 0
        right_pnt = len(heights) - 1
        max_water = 0

        while left_pnt < right_pnt:
            water = (right_pnt - left_pnt) * min(heights[left_pnt], heights[right_pnt])
            max_water = max(water, max_water)

            if heights[left_pnt] < heights[right_pnt]:
                left_pnt += 1
            else:
                right_pnt -= 1

        return max_water

        