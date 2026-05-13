class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        '''

        Input: nums = [2,20,4,10,3,4,5]

        Output: 4.  (2,3,4,5)

        '''

        # Run step by step / Visualize to solve easily, first find the start of the sequnce and then the increments there from for that num
        # calculations start only from the start of the sequence

        nums_set = set(nums)        # Create a set to compare the values

        longest_seq = 0             # Variable to check and update as the longest sequence gets found


        for num in nums:
            if (num - 1) not in nums_set:               # check if it could be the start of a sequence, if not, just move to seoncd element 
                length = 0                              # but if the start of the sequence is found, keep checking if the current value + 1 exists in the set
                while (num + length) in nums_set:
                    length += 1                         # keep checking for sequence +1
                longest_seq = max(length, longest_seq)  # once it comes out, update the longest sequence if it more than the previous

        return longest_seq