from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = [0 for i in range(len(nums) + 1)]
        presum_map = defaultdict(int)
        presum_map[0] = 1
        count = 0
        for i in range(1, len(nums) + 1):
            presum[i] = presum[i-1] + nums[i-1]
        for i in range(1, len(nums)+1):
            count += presum_map[presum[i] - k]
            presum_map[presum[i]] += 1
        return count

