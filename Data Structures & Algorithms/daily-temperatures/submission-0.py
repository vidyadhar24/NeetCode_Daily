class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)   # defulat wait time as 0 for all days
        stack = []   # element is a pair:[idx, temp]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:  # compare the the top of the stack
                stack_idx, stack_t = stack.pop()
                res[stack_idx] = i - stack_idx
            stack.append([i, t])
        return res

        '''
        Solution:

        Example: [1, 4, 1, 2, 1, 0, 0]

        Initial temperatures: [30, 38, 30, 36, 35, 40, 28]
        --- Day 0: Temperature 30 ---
        [+] Pushed Day 0 (30) to stack.
        Current Stack:  [[0, 30]]
        Current Result: [0, 0, 0, 0, 0, 0, 0]

        --- Day 1: Temperature 38 ---
        [!] Warmer day found! Day 1 (38) is warmer than Day 0 (30).
            Day 0 waited 1 day(s). Popped from stack.
        [+] Pushed Day 1 (38) to stack.
        Current Stack:  [[1, 38]]
        Current Result: [1, 0, 0, 0, 0, 0, 0]

        --- Day 2: Temperature 30 ---
        [+] Pushed Day 2 (30) to stack.
        Current Stack:  [[1, 38], [2, 30]]
        Current Result: [1, 0, 0, 0, 0, 0, 0]

        --- Day 3: Temperature 36 ---
        [!] Warmer day found! Day 3 (36) is warmer than Day 2 (30).
            Day 2 waited 1 day(s). Popped from stack.
        [+] Pushed Day 3 (36) to stack.
        Current Stack:  [[1, 38], [3, 36]]
        Current Result: [1, 0, 1, 0, 0, 0, 0]

        --- Day 4: Temperature 35 ---
        [+] Pushed Day 4 (35) to stack.
        Current Stack:  [[1, 38], [3, 36], [4, 35]]
        Current Result: [1, 0, 1, 0, 0, 0, 0]

        --- Day 5: Temperature 40 ---
        [!] Warmer day found! Day 5 (40) is warmer than Day 4 (35).
            Day 4 waited 1 day(s). Popped from stack.
        [!] Warmer day found! Day 5 (40) is warmer than Day 3 (36).
            Day 3 waited 2 day(s). Popped from stack.
        [!] Warmer day found! Day 5 (40) is warmer than Day 1 (38).
            Day 1 waited 4 day(s). Popped from stack.
        [+] Pushed Day 5 (40) to stack.
        Current Stack:  [[5, 40]]
        Current Result: [1, 4, 1, 2, 1, 0, 0]
        
        --- Day 6: Temperature 28 ---
        [+] Pushed Day 6 (28) to stack.
        Current Stack:  [[5, 40], [6, 28]]
        Current Result: [1, 4, 1, 2, 1, 0, 0]
        Final Output: [1, 4, 1, 2, 1, 0, 0]
        '''