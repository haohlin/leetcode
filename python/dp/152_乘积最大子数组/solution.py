from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_mul = nums[0]
        max_i = min_i = 1

        for n in nums:
            if n < 0:
                max_i, min_i = min_i, max_i
            max_i = max(max_i * n, n)
            min_i = min(min_i * n, n)

            max_mul = max(max_mul, max_i)
        return max_mul
