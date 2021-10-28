# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = [root]
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    for node in queue:
                        if node:
                            return False
                    return True