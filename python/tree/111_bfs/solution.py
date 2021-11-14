import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        depth = 0
        while q:
            depth += 1
            for i in range(len(q)):
                r = q.pop(0)
                if not r.left and not r.right:
                    return depth
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            