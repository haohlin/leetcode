from typing import List

class Solution1:
    def trap(self, height: List[int]) -> int:
        vol = 0
        max_left = [0 for i in range(len(height))]
        max_right = [0 for i in range(len(height))]
        max_left[0] = height[0]
        max_right[len(height)-1] = height[len(height)-1]
        for l in range(1, len(height)):
            max_left[l] = max(max_left[l-1], height[l])
        for r in reversed(range(len(height) - 1)):
            max_right[r] = max(max_right[r+1], height[r])
        for i in range(len(height)):
            min_lr = min(max_left[i], max_right[i])
            vol += min_lr - height[i]
        return vol

class Solution2:
    def trap(self, height: List[int]) -> int:
        left = 0
        left_max = -1
        right_max = -1
        right = len(height) - 1
        i = 0
        trap = 0
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max <= right_max:
                trap += left_max - height[left]
                left += 1
            else:
                trap += right_max - height[right]
                right -= 1
            
        return trap