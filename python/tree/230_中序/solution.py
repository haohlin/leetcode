from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution1:
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

class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            self.count += 1
            if self.count == k:
                self.result = root.val
            inorder(root.right)
            return
        self.result = 0
        self.count = 0
        inorder(root)

        return self.result