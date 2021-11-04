from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            if i > len(nums) - 1:
                return
            for j in range(i, len(nums)):
                res_i.append(nums[j])
                res = res_i.copy()
                result.append(res)
                backtrack(j + 1)
                res_i.pop()
            return
        result = [[]]
        res_i = []
        backtrack(0)
        return result