from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if len(res_i) == len(nums):
                res = res_i.copy()
                result.append(res)
                return
            for i in range(len(nums)):
                if nums[i] in res_i:
                    continue
                res_i.append(nums[i])
                backtrack()
                res_i.pop()
            return
        result = []
        res_i = []
        backtrack()
        return result
