from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        result = []
        temp = root
        while stack or temp:
            while temp:
                result.append(temp.val)
                stack.append(temp)
                temp = temp.left
            p = stack.pop()
            if p.right:
                temp = p.right
        return result