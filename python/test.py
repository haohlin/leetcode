class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

class Solution:
    def maxPath(self, root: TreeNode) -> int:
        if root == None:
            return -1
        max_left = self.maxPath(root.left)
        max_right = self.maxPath(root.right)
        return max(max_left, max_right) + 1
        


n4 = TreeNode()
n3 = TreeNode(None, n4)
n1 = TreeNode()
n2 = TreeNode(n3, n4)
root = TreeNode(n1, n2)

sol = Solution()
result = sol.maxPath(root)
print(result)