class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j+1]: 
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums