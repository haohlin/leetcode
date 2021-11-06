from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[[0, 0] for i in range(k+1)] for j in range(len(prices))]
        for i in range(len(prices)):
            for j in range(1, k+1):
                if i == 0:
                    dp[i][j][1] = -prices[0]
                    continue
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[-1][-1][0]