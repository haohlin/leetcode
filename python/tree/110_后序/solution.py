# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        bal, _ = self.helper(root)
        return bal
    
    def helper(self, root):
        if root == None:
            return True, 0
        l_bal, l_h = self.helper(root.left)
        r_bal, r_h = self.helper(root.right)
        cur_h = max(l_h + 1, r_h + 1)
        if l_bal and r_bal and abs(l_h - r_h) <=1:
            return True, cur_h
        else:
            return False, cur_h