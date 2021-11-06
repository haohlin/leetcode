from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums1 = nums[:-1]
        nums2 = nums[1:]
        return max(self.maxProfit(nums1), self.maxProfit(nums2))
    
    def maxProfit(self, nums):
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]