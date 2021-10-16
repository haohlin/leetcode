from collections import defaultdict
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)
        for n in nums:
            hash_map[n] += 1
            
        return list(hash_map.keys())[list(hash_map.values()).index(1)]