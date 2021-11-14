from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [-1, -1]
        for n in nums:
            if nums[abs(n)-1] > 0:
                nums[abs(n)-1] = -nums[abs(n)-1]
            else:
                result[0] = abs(n)
        for i, n in enumerate(nums):
            if n > 0:
                result[1] = i + 1
        return result