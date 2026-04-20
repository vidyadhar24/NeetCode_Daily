class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Dictionary to save the seen items
        seen_dict = {}
        result = []

        for idx, num in enumerate(nums):
            if not seen_dict: # if dict is empty
                seen_dict[num] = idx
            else:
                other_num  = target - num
                if other_num in seen_dict:
                    result.append(idx)
                    result.append(seen_dict[other_num])
                    result.sort()
                    return result
                else:
                    seen_dict[num] = idx

