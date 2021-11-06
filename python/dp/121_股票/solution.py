from typing import List

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for i in range(len(prices))]
        for i in range(1, len(prices)):
            dp[i] =  max(0, dp[i-1] + prices[i] - prices[i-1])
        return max(dp)
        
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for i in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][0] = 0
        for i in range(1, len(prices)):
            dp[i][0] =  max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] =  max(dp[i-1][1], -prices[i])
        return dp[-1][0]

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        profit_1 = -prices[0]
        profit_0 = 0
        for i in range(1, len(prices)):
            profit_0 =  max(profit_0, profit_1 + prices[i])
            profit_1 =  max(profit_1, -prices[i])
        return profit_0