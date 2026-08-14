class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                l, r = i + 1, len(nums) - 1

                # implement two sum
                while l < r:
                    sum_of_three = n + nums[l] + nums[r]
                    if sum_of_three < 0:
                        l += 1
                    elif sum_of_three > 0:
                        r -= 1
                    else:
                        result.append([n, nums[l], nums[r]])
                        l += 1

                        while nums[l] == nums[l -1] and l < r:
                            l += 1

        return result