import math
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + int((right - left) / 2)
            if self.getNum(nums, mid - 1) < self.getNum(nums, mid) > self.getNum(nums, mid + 1):
                return mid
            elif self.getNum(nums, mid - 1) > self.getNum(nums, mid):
                right = mid - 1
            elif self.getNum(nums, mid - 1) < self.getNum(nums, mid):
                left = mid + 1
    
    def getNum(self, nums, i):
        if i == -1 or i == len(nums):
            return -math.inf
        else:
            return nums[i]