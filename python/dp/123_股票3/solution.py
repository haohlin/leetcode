from typing import List

class Solution1: # 90% AC
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = len(prices) - 1
        profits = []
        while sell > 0:
            while buy >= 1 and prices[buy-1] < prices[buy]:
                buy -= 1
            profit_i = prices[sell] - prices[buy]
            profits.append(profit_i)
            sell = buy - 1
            buy = sell
        profits.sort(reverse=True)

        return sum(profits[:2])

class Solution2: # 100% AC
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[0, 0] for i in range(3)] for j in range(len(prices))]
        dp[0][1] = dp[0][2] = [0, -prices[0]]
        for i in range(1, len(prices)):
            for k in range(1, 3):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[-1][-1][0]