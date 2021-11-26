from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root):
            if not root:
                return 
            
            inorder(root.right)
            self.cur_sum += root.val
            root.val = self.cur_sum
            inorder(root.left)
            return 

        self.cur_sum = 0
        inorder(root)
        return root
