from typing import List
import math

class Solution:
    def sortArray(self, nums: List[int], left=None, right=None) -> List[int]:
        min_num = min(nums)
        max_num = max(nums)
        diff = max_num - min_num
        if diff == 0:
            return nums

        n_bucket = 10
        bucket_intg = diff / n_bucket
        buckets = []

        for i in range(n_bucket + 1):
            buckets.append([])

        for e in nums:
            bucket_idx = math.floor((e - min_num) / bucket_intg)
            self.insert(buckets[bucket_idx], e)
        
        result = []
        for buc in buckets:
            result += buc
        return result

    def insert(self, bucket, num):
        if not bucket:
            bucket.append(num)
        else:
            for i in reversed(range(len(bucket))):
                if num > bucket[i]:
                    bucket.insert(i + 1, num)
                    break
                if i == 0:
                    bucket.insert(i, num)

sol = Solution()
results = sol.sortArray([-74,48,-20,2,10,-84,-5,-9,11,-24,-91,2,-71,64,63,80,28,-30,-58,-11,-44,-87,-22,54,-74,-10,-55,-28,-46,29,10,50,-72,34,26,25,8,51,13,30,35,-8,50,65,-6,16,-2,21,-78,35,-13,14,23,-3,26,-90,86,25,-56,91,-13,92,-25,37,57,-20,-69,98,95,45,47,29,86,-28,73,-44,-46,65,-84,-96,-24,-12,72,-68,93,57,92,52,-45,-2,85,-63,56,55,12,-85,77,-39])
print(results)