from collections import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        stack = []
        for i in reversed(range(len(temperatures))):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            result[i] = 0 if not stack else stack[-1][1] - i
            stack.append([temperatures[i], i])
        return result
            