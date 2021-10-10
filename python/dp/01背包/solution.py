
import math

class Solution:
    def knapsack(self , V , n , vw ):
        # write code here
        dp = [0 for i in range (V + 1)]
        for i in range(len(vw)):
            vi = vw[i][0]
            wi = vw[i][1]
            for j in reversed(range(V + 1)):
                if j - vi >= 0:
                    dp[j] = max(dp[j], dp[j - vi] + wi)
        return dp[V]