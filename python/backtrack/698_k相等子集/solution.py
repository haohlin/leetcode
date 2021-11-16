from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def backtrack(i):
            if i == len(nums):
                for sum_i in result:
                    if sum_i != target:
                        return False
                return True

            for j in range(k):
                if result[j] + nums[i] > target:
                    continue
                result[j] += nums[i]
                if backtrack(i + 1):
                    return True
                result[j] -= nums[i]
            return False

        if sum(nums) % k != 0:
            return False
        target = sum(nums) / k
        result = [0 for i in range(k)]
        nums.sort(reverse=True)
        res = backtrack(0)
        return res