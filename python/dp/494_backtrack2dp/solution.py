from typing import List

class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp = dict()
        res = self.backtrack(nums, target, 0)
        return res

    def backtrack(self, nums, target, idx):
        if idx == len(nums):
            if target == 0:
                return 1
            return 0

        if (idx, target) in self.dp:
            return self.dp[(idx, target)]

        result_p = self.backtrack(nums, target - nums[idx], idx + 1)
        result_m = self.backtrack(nums, target + nums[idx], idx + 1)

        res = result_p + result_m
        self.dp[(idx, target)] = res

        return res

class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sub_sum = sum(nums) + target
        if sum(nums) < abs(target) or (sub_sum) % 2 == 1:
            return 0
        sub_sum = int(sub_sum / 2)

        dp = [[0 for j in range(sub_sum + 1)] for i in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(sub_sum + 1):
                if nums[i - 1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i - 1]]
        
        return dp[-1][-1]

class Solution3:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sub_sum = sum(nums) + target
        if sum(nums) < abs(target) or (sub_sum) % 2 == 1:
            return 0
        sub_sum = int(sub_sum / 2)

        dp = [0 for j in range(sub_sum + 1)]
        dp[0] = 1
        for i in range(1, len(nums) + 1):
            for j in reversed(range(sub_sum + 1)):
                if nums[i - 1] > j:
                    dp[j] = dp[j]
                else:
                    dp[j] = dp[j] + dp[j-nums[i - 1]]
        
        return dp[-1]
