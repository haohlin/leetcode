from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_list = []
        self.getList(root, sorted_list)
        print(sorted_list)
        return sorted_list[k-1]

    def getList(self, root, l):
        if not root:
            return
        self.getList(root.left, l)
        l.append(root.val)
        self.getList(root.right, l)
        return