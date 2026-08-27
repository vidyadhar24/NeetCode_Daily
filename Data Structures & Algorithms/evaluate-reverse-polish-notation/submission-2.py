class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:
            if t == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))

        return stack[0]

"""
[ INITIAL STATE ] 
Tokens:  ["2", "1", "+", "3", "*"]
Stack:   |   | (Empty)
         +---+

----------------------------------------------------
[ STEP 1 ] 
Current Token: "2" (Number)
Action: Push to stack

Stack:   |   |
         |   |
         |_2_| 

----------------------------------------------------
[ STEP 2 ] 
Current Token: "1" (Number)
Action: Push to stack

Stack:   |   |
         | 1 | <-- Top
         |_2_| 

----------------------------------------------------
[ STEP 3 ] 
Current Token: "+" (Operator)
Action: Pop 'a' (1), Pop 'b' (2). 
Math:   b + a  ->  2 + 1 = 3. Push 3.

Stack:   |   |
         |   |
         |_3_| <-- Top (Result of 2+1)

----------------------------------------------------
[ STEP 4 ] 
Current Token: "3" (Number)
Action: Push to stack

Stack:   |   |
         | 3 | <-- Top
         |_3_| 

----------------------------------------------------
[ STEP 5 ] 
Current Token: "*" (Operator)
Action: Pop 'a' (3), Pop 'b' (3). 
Math:   b * a  ->  3 * 3 = 9. Push 9.

Stack:   |   |
         |   |
         |_9_| <-- Top (Final Result)


Numbers go in: If the token is a number, always push it onto the stack.

Operators trigger math: If the token is an operator, pop the top two elements from the stack.

Order matters heavily: The first popped element is the right operand (a), and the second popped is the left operand (b). Calculate b [operator] a (crucial for - and /).

Result goes back: Push the evaluated mathematical result back onto the stack to be used by future operators.

Final Answer: At the end of the token list, exactly one item will remain in the stack—this is your final answer (stack[0]).

"""
