from typing import List

class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
           res ^= nums[i]
           res ^= i
        return res ^ len(nums)

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        result = [False for i in range(len(nums) + 1)]
        for n in nums:
            result[n] = True
        for i, r in enumerate(result):
            if not r:
                return i

class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(list(range(len(nums) + 1))) - sum(nums)

class Solution4:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(list(range(len(nums) + 1))) - sum(nums)