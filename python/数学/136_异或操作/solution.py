from collections import defaultdict
from typing import List

class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        res = defaultdict(int)
        for n in nums:
            res[n] += 1
            if res[n] > 1:
                del res[n]
        for k,v in res.items():
            return k