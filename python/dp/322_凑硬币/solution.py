import math
from typing import List

class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(amt):
            if amt in dp_list:
                return dp_list[amt]
            if amt == 0: 
                return 0
            if amt < 0:
                return -1

            temp = math.inf

            for coin in coins:
                sub_best = dp(amt - coin)
                if sub_best == -1:
                    continue
                temp = min(temp, 1 + sub_best)
            dp_list[amt] = temp if temp != math.inf else -1
            

            return dp_list[amt]



        dp_list = dict()
        num = dp(amount)
        return num

class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for i in range(amount + 1)] # amount + 1 or math.inf
        dp[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1