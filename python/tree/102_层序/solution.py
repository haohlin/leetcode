from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        results = []
        while stack:
            result_i = []
            for i in range(len(stack)):
                p = stack.pop(0)
                result_i.append(p.val)
                if p.left:
                    stack.append(p.left)
                if p.right:
                    stack.append(p.right)
            results.append(result_i)
        return results