from typing import List
import math

class Solution:
    def sortArray(self, nums):
        inc = round(len(nums) / 2)
        while inc >= 1:
            for i in range(inc):
                for j in range(i,len(nums),inc):
                    temp = nums[j]
                    for k in reversed(range(i, j, inc)):
                        if temp < nums[k]:
                            nums[k+inc], nums[k] = nums[k], nums[k+inc]
                        
            inc = round(inc / 2)
        return nums

sol = Solution()
results = sol.sortArray([1,2,6,3,2,5,3,4,5])
print(results)