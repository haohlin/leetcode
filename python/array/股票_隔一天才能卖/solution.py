# 隔一天才能卖

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for i in range(len(prices))]
        for i in range(2, len(prices)):
            sell = i
            buy = sell - 2
            while buy > 0 and prices[buy] >= prices[buy-1]:
                buy -= 1
            if buy >= 1:
                dp[i] = dp[buy - 1] + prices[sell] - prices[buy]
            else:
                dp[i] = prices[sell] - prices[buy]
        return max(dp)
