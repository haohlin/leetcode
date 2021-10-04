from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left1 = left2 = 0
        right1 = right2 = len(nums) - 1
        if not nums:
            return [-1,-1]

        while left1 <= right1 or left2 <= right2:
            if left1 <= right1:
                mid1 = round((left1 + right1) / 2)
                if nums[mid1] >= target:
                    right1 = mid1 - 1
                elif nums[mid1] < target:
                    left1 = mid1 + 1

            if left2 <= right2:
                mid2 = round((left2 + right2) / 2)
                if nums[mid2] <= target:
                    left2 = mid2 + 1
                elif nums[mid2] > target:
                    right2 = mid2 - 1

        if left1 > len(nums) - 1 or nums[left1] != target:
            return [-1, -1]
        
        return [left1, right2]