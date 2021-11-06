from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        while i <= len(nums) - 3:
            n = nums[i]
            result_i = self.twoSum(nums[i+1:], -n)
            for res_i in result_i:
                res_i.append(n)
                result.append(res_i)
            while i <= len(nums) - 3 and nums[i] == n:
                i += 1
        return result

    def twoSum(self, nums, target):
        slow = 0
        fast = len(nums) - 1
        result = []
        while slow < fast:
            sum_i = nums[slow] + nums[fast]
            slow_n = nums[slow]
            fast_n = nums[fast]
            if sum_i == target:
                result.append([slow_n, fast_n])
                while slow < len(nums) and nums[slow] == slow_n:
                    slow += 1
                while fast >= 0 and nums[fast] == fast_n:
                    fast -= 1
            elif sum_i < target:
                while slow < len(nums) and nums[slow] == slow_n:
                    slow += 1
            elif sum_i > target:
                while fast >= 0 and nums[fast] == fast_n:
                    fast -= 1
        return result