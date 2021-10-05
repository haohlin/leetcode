from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        nums_sorted = sorted(nums) # sort the array
        while left <= right:
            cur = nums_sorted[left] + nums_sorted[right]
            if cur == target:
                # find the index in the original array (can't be same index)
                return [nums.index(nums_sorted[left]), len(nums) - nums[::-1].index(nums_sorted[right]) - 1] 
            elif cur < target:
                left += 1
            elif cur > target:
                right -= 1
        return -1