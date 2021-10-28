from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        slow = 0
        fast = 1
        max_len = 1
        while fast < len(nums):
            if nums[fast] == nums[fast - 1] + 1:
                max_len = max(max_len, fast + 1 - slow)
            else:
                slow = fast
            fast += 1
        return max_len