from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def dfs(root):
            if not root:
                return 0
            if root in dp:
                return dp[root]
            robbed_left = dfs(root.left.left) + dfs(root.left.right) if root.left else 0
            robbed_right = dfs(root.right.left) + dfs(root.right.right) if root.right else 0
            robbed = root.val + robbed_left + robbed_right

            not_robbed = dfs(root.left) + dfs(root.right)
            res = max(robbed, not_robbed)
            dp[root] = res
            return res
            
        dp = dict()
        return dfs(root)
