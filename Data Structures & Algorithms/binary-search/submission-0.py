class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums = [-1,0,2,4,6,8], target = 4

        #  0 1 2 3 4 5
        # -1 0 2 4 6 8

        
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            mid_idx = (left_pointer + right_pointer) // 2
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] > target:
                right_pointer = mid_idx - 1
            else:
                left_pointer = mid_idx + 1

        return -1


