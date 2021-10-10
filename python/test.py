import math
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp():
            if sum(coin_list) == amount:
                self.min_count = min(len(coin_list), self.min_count)
                return
            for c in coins:
                coin_list.append(c)
                if sum(coin_list) <= amount:
                    dp()
                coin_list.pop()
            return

        
        self.min_count = math.inf
        coin_list = []
        dp()
        return self.min_count

sol = Solution()
result = sol.coinChange([5,2,1], 11)
print(result)