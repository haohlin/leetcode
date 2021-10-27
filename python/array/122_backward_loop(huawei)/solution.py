from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = len(prices) - 1
        rev = 0
        while i > 0:
            j = i
            min_right_idx = i
            min_left_idx = j
            while prices[j - 1] < prices[j] and j > 0:
                j -= 1
            min_left_idx = j
            rev += prices[min_right_idx] - prices[min_left_idx]
            i = j - 1
        return rev