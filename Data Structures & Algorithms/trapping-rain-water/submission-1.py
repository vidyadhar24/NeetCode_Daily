class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        trapped_water = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                trapped_water += (left_max - height[l])
            
            else:
                r -= 1
                right_max = max(right_max, height[r])
                trapped_water += (right_max - height[r])

        return trapped_water

    '''
    ip = [0,2,0,3,1,0,1,3,2,1]
    result expected = 9

    Exp:

    3 |          [] ~~ ~~ ~~ []       
    2 |    [] ~~ [] ~~ ~~ ~~ [] []    
    1 |    [] ~~ [] [] ~~ [] [] [] [] 
    --+-------------------------------
      |  0  2  0  3  1  0  1  3  2  1

    [] = Elevation Block  |  ~~ = Trapped Water

    1. The key is find out the water held at each point
    2. How to do that:
        - Use formula -> min(max(left), max(right)) - current point 
        - and consider value > 0
        - at point 2  -> min(0, 3) - 2 = -2
        - at point 0 / indx 2 -> min(2, 3) - 0 = 2

    3. Now, how to apply this:
        - use two pointers left and right
        - two variables to get the max from left and max from right
        - Now, start from a poin and keep applying the above formula
            - this will be applied from left side and from right side too.. depending upon the min(left_max, right_max)
        - let's move to second point (2) to understand this better
         - at point 2, left_max = 0, right max = 1
            - but this right max is not the actual max to the right.. that is correct..
            - But, since we are taking the MIN of maxes of left and right, and we already know that left_max < right_max (hence we are at this step actually), there is no point in checking for the actual right max. it IS GOING TO BE > left max
            - same is the case with right side too..
            - we start coming from right side, when the right_max < left_max.. hence we would not need actual left max
         - so, simply at point 2 : min(0, 1) - 2 = -2
         - at point with value 0 (idx 2): min(2, 3) - 0 = 2
         - Thus, trapped water will be calculated each step 
 

    '''

