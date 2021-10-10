# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param root TreeNode类 
# @param o1 int整型 
# @param o2 int整型 
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root , o1 , o2 ):
        node = self.helper(root, o1, o2)
        if not node:
            return -1
        
        return node.val
    def helper(self, root , o1 , o2 ):
        if not root:
            return None
        elif root.val == o1 or root.val == o2:
            return root
        left = self.helper(root.left, o1, o2)
        right = self.helper(root.right, o1, o2)
        if left and right:
            return root
        elif left and not right:
            return left
        elif not left and right:
            return right
        elif not left and not right:
            return None