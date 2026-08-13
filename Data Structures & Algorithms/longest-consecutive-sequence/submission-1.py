class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest_seq = 0

        for num in nums:
            if (num - 1) not in nums_set:
                length = 0

                while (num + length) in nums_set:
                    length += 1
                longest_seq = max(length, longest_seq)

        return longest_seq
                