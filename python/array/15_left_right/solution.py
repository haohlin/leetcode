from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(start, target, nThree):
            left = start
            right = len(nums) - 1
            result_2 = []
            while left < right:
                sumLR = nums[left] + nums[right]
                left_num = nums[left]
                right_num = nums[right]
                if sumLR < target:
                    while left < right and nums[left] == left_num:
                        left += 1
                elif sumLR > target:
                    while left < right and right_num == nums[right]:
                        right -= 1
                else:
                    result_2.append([nThree, left_num, right_num])
                    while left < right and right_num == nums[right]:
                        right -= 1
                    while left < right and nums[left] == left_num:
                        left += 1
            return result_2


        nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            numThree = nums[i]
            two_sum_target = -numThree
            two_result = twoSum(i + 1, two_sum_target, numThree)
            if not two_result:
                continue
            for r in two_result:
                result.append(r)
        return result
