from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, left, right):
        if right <= left:
            return None
        mid = self.partition(nums, left, right)
        self.quickSort(nums, left, mid - 1)
        self.quickSort(nums, mid + 1, right)
        return

    def partition(self, nums, left, right):
        pivit = nums[left]
        j = left
        for i in range(left + 1, right + 1):
            if nums[i] <= pivit:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        nums[left], nums[j] = nums[j], nums[left]
        return j
            
nums = [-74,48,-20,2,10,-84,-5,-9,11,-24,-91,2,-71,64,63,80,28,-30,-58,-11,-44,-87,-22,54,-74,-10,-55,-28,-46,29,10,50,-72,34,26,25,8,51,13,30,35,-8,50,65,-6,16,-2,21,-78,35,-13,14,23,-3,26,-90,86,25,-56,91,-13,92,-25,37,57,-20,-69,98,95,45,47,29,86,-28,73,-44,-46,65,-84,-96,-24,-12,72,-68,93,57,92,52,-45,-2,85,-63,56,55,12,-85,77,-39]
solution = Solution()
sol = solution.sortArray(nums)
print(sol)