from typing import List 

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_a = m
        min_b = n
        for op_i in ops:
            min_a = min(min_a, op_i[0])
            min_b = min(min_b, op_i[1])
        return min_a * min_b