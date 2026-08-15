class Solution:
    def isValid(self, s: str) -> bool:

        # Solved in the first Go.. Came out to be efficient solution

        if not s or len(s) == 1: return False

        # ()[{}]
    
        pairs = {'(':')', '[':']', '{' :'}'}
        stack = []
        
        for i in s:
            if i in pairs.keys():
                stack.append(pairs[i])
            elif stack and i == stack[-1]:
                stack.pop()
            else:
                return False

        return True if not stack else False

        '''
        1. create a hash map to associate opening and closing
        2. Now, loop throught the items and see if the item is opening
            - if it is, then add the corresponding closing to the stack [ a list, to end of which we keep adding elements]
            - but, if the closing came first, we check if the stack is empty.. meaning a closing can't come without opening
            - So, if it a closing one, and stack is empty, we move to else, return False
            - if we find a closing match, we remove the same from the stack
            - finally, if the stack is empty, we found all the closing ones, else some remain

        '''

