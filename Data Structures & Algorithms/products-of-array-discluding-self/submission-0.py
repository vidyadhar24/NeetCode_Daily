class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # [2 , 3, 4]

        # [12, 8, 6]

        prefix = 1
        result = [1] * len(nums)           #[1,1,1]

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]              # keep incrementally multiply the numbers in the list. 
                                           # at the end -> [1,2,6]. 12 won't be there as these are prefixes

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix            # by this time, all the prefixes are available, so multiple with the product from right side which     
            postfix *= nums[i]             # is calculated at this step

        return result



        