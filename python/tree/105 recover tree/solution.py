from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def builder(pre_start, pre_end, in_start, in_end):        
            if pre_start==pre_end or in_start==in_end:
                return None
            root = TreeNode(preorder[pre_start]) 

            root_idx_in = hashMap[root.val]
            left_in_start = in_start
            left_in_end = root_idx_in
            left_pre_start = pre_start + 1
            left_pre_end = left_pre_start + left_in_end - left_in_start 
            
            right_in_start = root_idx_in + 1
            right_in_end = in_end
            right_pre_start = left_pre_end
            right_pre_end = pre_end

            root.left = builder(left_pre_start, left_pre_end, left_in_start, left_in_end)
            root.right = builder(right_pre_start, right_pre_end, right_in_start, right_in_end)
            return root

        hashMap = {elem:i for i,elem in enumerate(inorder)}
        tree = builder(0, len(preorder), 0, len(inorder))
        return tree
