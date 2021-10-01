from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums))
        return nums

    def quickSort(self, ls, start, end):
        if start >= end:
            return
        midIdx = self.partition(ls, start, end)
        self.quickSort(ls, start, midIdx) 
        self.quickSort(ls, midIdx+1, end)
        return

    def partition(self, arr, start, end):
        midNum = arr[start]
        midIdx = start
        for i in range(start, end):
            if arr[i] < midNum:
                temp = arr[i]
                del arr[i]
                arr.insert(start, temp)
                midIdx += 1
        return midIdx

nums = [5,2,3,1]
solution = Solution()
sol = solution.sortArray(nums)
print(sol)