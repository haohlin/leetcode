# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        def getDepth(root):
            if not root:
                return 0
            return 1 + max(getDepth(root.left), getDepth(root.right))

        maxD = getDepth(root)
        return maxD

class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
        