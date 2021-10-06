import math
from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        fast = 0
        slow = 0
        count = 0
        max_num = -math.inf
        while fast < len(nums):
            max_num = max(max_num, nums[fast])
            if right < max_num or max_num < left:
                if fast == slow:
                    pass
                else:
                    count += math.factorial(fast - slow)
                slow = fast + 1
                max_num = -math.inf
            fast += 1
        
        count += math.factorial(fast - slow)
        return count

sol = Solution()
nums = [73,55,36,5,55,14,9,7,72,52]
l = 32
r = 69
c = sol.numSubarrayBoundedMax(nums, l, r)
print(c)