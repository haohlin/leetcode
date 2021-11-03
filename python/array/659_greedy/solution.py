from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        result = []
        for n in nums:
            inserted = False
            for res in result:
                if self.canInsert(res, n):
                    res.append(n)
                    inserted = True
                    break
            if not inserted:
                result.insert(0, [n])
        for res in result:
            if len(res) < 3:
                return False
        return True
        
    def canInsert(self, res, n):
        if not res or n == res[-1] + 1:
            return True
        else:
            return False