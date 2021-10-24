from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = 10 ** 9
        while left <= right:
            mid = left + round((right - left) / 2)
            mid_t = self.eatingTime(piles, mid)
            if mid_t <= h:
                right = mid - 1
            elif mid_t > h:
                left = mid + 1
        return left
    
    def eatingTime(self, piles, speed):
        t = 0
        for p in piles:
            t += math.ceil(p/speed)
        return t