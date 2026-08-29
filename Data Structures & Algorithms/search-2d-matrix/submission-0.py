class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
        '''
        1. first check if the items exists in any of the sub windows
        2. then apply the binary search in that window
        '''

        for l in matrix:
            if target >= l[0] and target <= l[-1]:
                li = 0
                mi = len(l) // 2
                ri = len(l) - 1

                while li <= ri:
                    if l[mi] == target:
                        return True
                    elif l[mi] > target:
                        ri = mi - 1
                    else: li = mi + 1
                    mi = (li + ri) // 2
                    
        return False