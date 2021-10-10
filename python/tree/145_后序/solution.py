from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        result = []
        temp = root
        while temp or stack:
            while temp:
                result.append(temp.val)
                stack.append(temp)
                temp = temp.right
            p = stack.pop()
            temp = p.left
        # result.reverse()
        return list(reversed(result))

class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        visited = False
        stack = [(visited, root)]
        while stack:
            visited, p = stack.pop()
            if not p:
                continue
            if not visited:
                visited = True
                stack.append((visited, p))
                stack.append((False, p.right))
                stack.append((False, p.left))
            else:
                result.append(p.val)
        return result