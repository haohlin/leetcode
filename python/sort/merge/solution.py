import math
from typing import List

class Solution:
    def merge(self, arr1: List[int], arr2: List[int]) -> List[int]:
        newArr = []
        while arr1 and arr2:
            if arr1[0] < arr2[0]:
                newArr.append(arr1.pop(0))
            else:
                newArr.append(arr2.pop(0))
        while arr1:
            newArr.append(arr1.pop(0))
        while arr2:
            newArr.append(arr2.pop(0))
        return newArr

    def sort(self, ls: List[int]) -> List[int]:
        if len(ls) < 2:
            return ls
        middle = math.floor((len(ls)) / 2)
        leftArr = ls[:middle]
        rightArr = ls[middle:len(ls)]
        return self.merge(self.sort(leftArr), self.sort(rightArr))

    def sortArray(self, nums: List[int]) -> List[int]:
        sorted = self.sort(nums)
        return sorted