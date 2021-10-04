import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
     
class Solution:
    def __init__(self) -> None:
        self.maxP = -math.inf
    def maxPathSum(self, root: TreeNode) -> int:
        def maxFinder(r):
            if not r:
                return 0
            leftMax = max(maxFinder(r.left), 0) 
            rightMax = max(maxFinder(r.right), 0)
            self.maxP = max(self.maxP, leftMax + rightMax + r.val)
            return max(leftMax, rightMax) + r.val
        rootMax = maxFinder(root)
        return self.maxP

sol = Solution()
root = TreeNode()
print(sol.maxPathSum(root))