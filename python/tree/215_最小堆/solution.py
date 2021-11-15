import copy
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        obj = Heap(nums, k)
        for n in nums[k:]:
            obj.add(n)
        return obj.getSmallest()

class Heap:
    def __init__(self, data, k):
        self.data = copy.deepcopy(data[:k])
        self.k = k
        for i in reversed(range(self.k - 1)):
            self.sink(i)

    def getSmallest(self):
        return self.data[0]

    def add(self, a):
        if a > self.data[0]:
            self.data[0] = a 
            self.sink(0)
    
    def sink(self, i):
        left = i * 2 + 1
        right = i * 2 + 2
        if left >= self.k:
            return
        
        if right >= self.k and self.data[i] > self.data[left]:
            self.data[i], self.data[left] = self.data[left], self.data[i]
            self.sink(left)
            return
        
        if right < self.k:
            smaller_child = right if self.data[left] > self.data[right] else left
            if self.data[i] > self.data[smaller_child]:
                self.data[i], self.data[smaller_child] = self.data[smaller_child], self.data[i]
                self.sink(smaller_child)
            return

    def swim(self, i):
        if i == 1:
            return 
        if self.data[i // 2] > self.data[i]:
            self.data[i // 2], self.data[i] = self.data[i], self.data[i // 2]
            self.swim(i // 2)
        else:
            return