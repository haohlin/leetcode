from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(prev_i):
            if len(res_i) == k:
                res = res_i.copy()
                result.append(res)
                return
            for i in range(prev_i+1, n+1):
                res_i.append(i)
                backtrack(i)
                res_i.pop()
            return

        result = []
        res_i = []
        backtrack(0)
        return result