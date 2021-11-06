from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict()
        two_sum = TwoSum()
        for i in range(len(nums)):
            two_sum.add(nums[i])
        return two_sum.find(target)

class TwoSum:
    def __init__(self, nums=[]):
        self.nums = nums
        self.sum = dict()

    def add(self, n):
        for i in range(len(self.nums)):
            self.sum[self.nums[i] + n] = [i, len(self.nums)]
        self.nums.append(n)

    def find(self, target):
        if target in self.sum:
            return self.sum[target]
        else:
            return [-1, -1]
