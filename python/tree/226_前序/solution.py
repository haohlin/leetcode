# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root

class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        temp_right = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp_right
        return root