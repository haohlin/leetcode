from typing import List 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow = 0
        fast = len(numbers) - 1
        while slow < fast:
            cur_sum = numbers[slow] + numbers[fast]
            if cur_sum == target:
                return [slow, fast]
            elif cur_sum > target:
                fast -= 1
            elif cur_sum < target:
                slow += 1
        return [-1, -1]