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
    
        '''
        Input: height = [1,7,2,5,4,7,3,6]

        Output: 36

        1. Using two pointers, we can solve this
        2. first we start from left and then right
        3. calcuate the area between these two points using
            (right -left) * min(right_value, left_value)
            right - left gives us the distance
            and then since we have to take the lowest (as water can be stored) of two values from these points
        4. Use a variable to keep checking for the big area
        5. IMP. --> moving the pointers

            - MOVE THE POINTER WHERE THE VALUE IS LESS
            - if the left value is less, increment the left pointer by 1
            - if the right one is less, decrement the same by one
            - Because, we are searching for a large area possible, hence moving away from the low value



        '''