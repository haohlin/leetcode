from typing import List

class Solution:
    def sortArray(self, nums: List[int], left=None, right=None) -> List[int]:
        diff = max(nums) - min(nums)
        min_num = min(nums)
        temp = [0] * (diff + 1)
        result = []
        for e in nums:
            temp[e - min_num] += 1
        for i in range(diff + 1):
            if temp[i] != 0:
                result += [i + min_num] * temp[i]
        return result