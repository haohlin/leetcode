from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = nums[0]
        for i in nums[1:]:
            diff ^= i
        b_1 = self.findIdxOfOneInBin(diff)
        num_1 = num_2 = 0
        for n in nums:
            if n & b_1 != 0:
                num_1 ^= n
            else:
                num_2 ^= n
        return [num_1, num_2]

    
    def findIdxOfOneInBin(self, n):
        res = 1
        while not res & n:
            res <<= 1 
        return res
    