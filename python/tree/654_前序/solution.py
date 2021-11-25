from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        root = self.maxTree(nums, 0, len(nums) - 1)
        return root

    def maxTree(self, nums, left, right):
        if left > right:
            return None
        
        max_n = -1
        max_i = -1
        for i in range(left, right + 1):
            if nums[i] > max_n:
                max_n = nums[i]
                max_i = i

        new_node = TreeNode(max_n)

        new_node.left = self.maxTree(nums, left, max_i - 1)
        new_node.right = self.maxTree(nums, max_i + 1, right)

        return new_node
