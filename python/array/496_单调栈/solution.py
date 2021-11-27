from collections import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result2 = [0 for i in range(len(nums2))]
        result1 = [0 for i in range(len(nums1))]
        stack = []
        for i in reversed(range(len(nums2))):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            result2[i] = -1 if not stack else stack[-1]
            stack.append(nums2[i])

        for i in range(len(nums1)):
            result1[i] = result2[nums2.index(nums1[i])] 

        return result1