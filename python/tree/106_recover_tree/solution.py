from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.builder(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)

    def builder(self, inorder, postorder, in_start, in_end, post_start, post_end):
        if in_start > in_end:
            return None
        root_n = postorder[post_end]
        root_i = 0
        for i in range(in_start, in_end + 1):
            if inorder[i] == root_n:
                root_i = i
                break
        left_in_start = in_start
        left_in_end = root_i - 1
        left_post_start = post_start
        left_post_end = post_start + left_in_end - left_in_start
        right_in_start = root_i + 1
        right_in_end = in_end
        right_post_start = left_post_end + 1
        right_post_end = post_end - 1

        root = TreeNode(root_n)
        root.left = self.builder(inorder, postorder, left_in_start, left_in_end, left_post_start, left_post_end)
        root.right = self.builder(inorder, postorder, right_in_start, right_in_end, right_post_start, right_post_end)

        return root
