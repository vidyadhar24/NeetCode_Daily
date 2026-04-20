class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_dict = {}
        for num in nums:
            if num not in hash_dict:
                hash_dict[num] = 1
            else: 
                return True
        return False
        