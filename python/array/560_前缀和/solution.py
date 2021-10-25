from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(int)
        presum = [0 for i in range(len(nums) + 1)]
        count = 0
        for i in range(1, len(presum)):
            presum[i] = presum[i-1] + nums[i-1]
        for i in range(len(nums)+1):
            count += hash_map[presum[i] - k]
            hash_map[presum[i]] += 1
        return count
