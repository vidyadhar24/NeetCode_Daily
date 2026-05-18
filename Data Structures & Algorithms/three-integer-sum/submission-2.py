class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums.sort()
        result = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i -1]:   # if it is same num as previous, skip this
                continue
            else:
                l, r = i + 1, len(nums) - 1  # left pointer = idx + 1, right pointer last index

                while l < r:
                    threesum = n + nums[l] + nums[r]  # check if the three sum == 0
                    if threesum > 0:                   # if is > 0, meaning right value should be considered ( as left will be -ve or small numbers)
                        r -= 1  
                    elif threesum < 0:
                        l += 1
                    else:
                        result.append([n, nums[l], nums[r]])
                        l += 1                         # even when one solution is found, we keep incrementing the left to check for other possibilites
                        while nums[l] == nums[l -1] and l < r:
                            l += 1

        return result



        '''
        Input:  nums            =    [-1,0,1,2,-1,-4]
                sorted nums     =    [-4, -1, -1, 0, 1, 2]
                Expected output =    [[-1,-1,2],[-1,0,1]]

        1. Sort the array first
        2. then take the first one from the left (-4), then use the two sum method to find out if the two sum of the remaining elements + the current number == 0
        3. Since, this is sorted, going from left right, would do the trick
        4. Understand the following two parts to remove the duplicates..
            ex: [-1,-1,0,1,1,2]
            here solution -1, -1, 2 is possible twice, taking -1 once each time, but duplicate items are not allowed
            So, first check is the forloop checks for this.

            one more scenario, is even when one solution is found out, there can be one more as well.
            ex: [-1,-1,0,0,1,1], first we get, -1,0,1 and there can be one more of them same as well
            that is why is the last step, left pointed is skipped if the same number exists after finding one result with same number

        '''
