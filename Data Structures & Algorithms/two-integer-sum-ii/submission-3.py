class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        li = 0
        ri = len(numbers) - 1

        while li < ri:
            nums_sum = numbers[li] + numbers[ri]
            if nums_sum == target:
                return [li+1, ri+1]
            elif nums_sum < target:
                li += 1
                continue
            else:
                ri -= 1
        return []
