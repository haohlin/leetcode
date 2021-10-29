import math
from typing import List

class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums, left, right):
        if right - left + 1 == 1:
            return None
        mid = left + int((right - left) / 2)
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid+1, right)
        return self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        arr1 = nums[left:mid+1] # 直接赋值，指向同一块内存。.copy() 也可以
        ptr1 = 0
        arr2 = nums[mid+1:right+1]
        ptr2 = 0
        for i in range(left, right + 1):
            if ptr1 <= mid - left and ptr2 <= right - mid - 1:
                if arr1[ptr1] > arr2[ptr2]:
                    nums[i] = arr2[ptr2]
                    ptr2 += 1
                else:
                    nums[i] = arr1[ptr1]
                    ptr1 += 1
            elif ptr1 > mid - left:
                nums[i] = arr2[ptr2]
                ptr2 += 1
            elif ptr2 > right - mid - 1:
                nums[i] = arr1[ptr1]
                ptr1 += 1

sol = Solution()
results = sol.sortArray([-74,48,-20,2,10,-84,-5,-9,11,-24,-91,2,-71,64,63,80,28,-30,-58,-11,-44,-87,-22,54,-74,-10,-55,-28,-46,29,10,50,-72,34,26,25,8,51,13,30,35,-8,50,65,-6,16,-2,21,-78,35,-13,14,23,-3,26,-90,86,25,-56,91,-13,92,-25,37,57,-20,-69,98,95,45,47,29,86,-28,73,-44,-46,65,-84,-96,-24,-12,72,-68,93,57,92,52,-45,-2,85,-63,56,55,12,-85,77,-39])
results2 = sol.sortArray([-1,2,0])
print(results)