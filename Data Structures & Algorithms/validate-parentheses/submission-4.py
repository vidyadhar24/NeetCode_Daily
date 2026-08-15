class Solution:
    def isValid(self, s: str) -> bool:

        if not s or len(s) == 1: return False

        # ()[{}]
    
        pairs = {'(':')', '[':']', '{' :'}'}
        stack = []
        # ]}
        
        for i in s:
            if i in pairs.keys():
                stack.append(pairs[i])
            elif stack and i == stack[-1]:
                stack.pop()
            else:
                return False

        return True if not stack else False




        
        return True