class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

class Solution1:
    def helper(self, root, l):
        if root == None:
            return
        left = self.helper(root.left, l)
        l.append(root.val)
        right = self.helper(root.right, l)
        return
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        self.helper(root, l)
        return l



class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        pass