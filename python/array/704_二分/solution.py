from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + round((right - left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

class SolutionLeft:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + round((right - left)/2)
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if nums and nums[left] == target:
            return right + 1
        else: 
            return -1

class SolutionRight:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + round((right - left)/2)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] <= target:
                left = mid + 1
        if nums and nums[right] == target:
            return right
        else: 
            return -1

sol = SolutionRight()
res = sol.search([1,1,2,2,2], 3)
print(res)