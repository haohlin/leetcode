
from typing import List

class Solution:
    def max_heapify(self, heap, root, heap_len):
        p = root
        largest = root
        left, right = (largest << 1) + 1, (largest << 1) + 2

        if left < heap_len and heap[left] > heap[largest]:
            largest = left

        if right < heap_len and heap[right] > heap[largest]:
            largest = right

        if largest != root:
            heap[largest], heap[root] = heap[root], heap[largest]
            self.max_heapify(heap, largest, heap_len)
        
    def build_heap(self, heap):
        for i in reversed(range(len(heap))):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in reversed(range(len(nums))):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)
            
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums


sol = Solution()
print(sol.sortArray([5,3,2,4,1]))
