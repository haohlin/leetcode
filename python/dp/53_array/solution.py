from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = dp_0 = nums[0]
        for i in range(1,len(nums)):
            dp_1 = max(dp_0 + nums[i], nums[i])
            max_sum = max(max_sum, dp_1)
            dp_0 = dp_1
        return max_sum