from typing import List
import math

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n_bucket = 10
        min_num = min(nums)
        nums = [e - min_num for e in nums]
        max_digit = self.getDigits((abs(max(nums))))
        for d in range(max_digit):
            buckets = [[] for i in range(n_bucket)]
            for e in nums:
                bucket_idx = (e % (10 ** (d + 1))) // (10 ** d)
                buckets[bucket_idx].append(e)
            result = []
            for bucket in buckets:
                result += bucket
            nums = result
        
        nums = [e + min_num for e in nums]
        return nums

    def getDigits(self, n):
    # https://stackoverflow.com/questions/2189800/how-to-find-length-of-digits-in-an-integer

        if n > 0:
            digits = int(math.log10(n))+1
        elif n == 0:
            digits = 1
        else:
            digits = int(math.log10(-n))+2 # +1 if you don't count the '-' 
        return digits

nums = [-12,3,56,2,4,19,-1]
solution = Solution()
sol = solution.sortArray(nums)
print(sol)