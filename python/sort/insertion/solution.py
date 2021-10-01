from typing import List

def sortArray(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        for j in reversed(range(i+1)):
            if nums[i + 1] > nums[j]:
                nums.insert(j + 1, nums[i + 1])
                break
            if j == 0:
                nums.insert(j, nums[i + 1])
        del nums[i+2]
    return nums
