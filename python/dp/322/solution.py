import math
from typing import List

class Solution:
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
