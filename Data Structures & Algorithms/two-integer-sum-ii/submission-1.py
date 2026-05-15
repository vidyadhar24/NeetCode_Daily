class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Attempt 1
        # came out to be the efficient one

        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            if numbers[left_pointer] + numbers[right_pointer] == target:
                return[left_pointer + 1, right_pointer + 1]
            elif numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
            else:
                left_pointer += 1
        
        return []

        '''
        Input 1: numbers = [1,2,3,4], target = 3.  not that it is sorted array problem

        left create two pointers one starts from left one from the right

        step 1 :  1 + 4 = 5
        which is > target of 3
        So, come down a step from right side as that is the bigger number as it is sorted

        step 2 : 1 + 3 = 4
        the left and right pointed started at 0, hence add 1 and return them
        --------------------------------------------------

        Input 2: numbers = [1,2,3,4], target = 7.  not that it is sorted array problem

        s1: 1 + 4 = 5 | 5 < 7
        So, increase one from the left, as it is sorted

        s2: 2 + 4 = 6 | 6 < 7

        s3: 3 + 4 = 7 .. that's it!

        '''

        