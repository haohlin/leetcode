from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = left + round((right - left) / 2)
            mid_day = self.maxDay(weights, mid)
            if mid_day <= days:
                right = mid - 1
            elif mid_day > days:
                left = mid + 1
        return left

    def maxDay(self, weights, cap):
        sum_i = 0
        max_day = 1
        for w in weights:
            sum_i += w
            if sum_i > cap:
                sum_i = w
                max_day += 1
        return max_day


sol = Solution()
res = sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)
print(res)