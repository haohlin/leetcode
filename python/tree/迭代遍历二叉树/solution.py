from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:    
    def traverseTree(self, root):
        self.visited = defaultdict(int)
        stack = []
        self.moveLeft(stack, root)
        while stack:
            cur_node = stack[-1]
            # 中序遍历
            # print(cur_node.val)
            if not cur_node.right or self.visited[cur_node.right]:
                # 后序遍历
                print(cur_node.val)
                stack.pop()
                continue
            self.moveLeft(stack, cur_node.right)
                    
    def moveLeft(self, stack, root):
        while root:
            # 前序遍历
            # print(root.val)
            stack.append(root)
            self.visited[root] = 1
            root = root.left


"""
  1
2   3
 4

self.arr = [1,2,3,4]
"""
root = TreeNode(val=1)
node_1 = TreeNode(val=2)
node_2 = TreeNode(val=3)
node_3 = TreeNode(val=4)
root.left = node_1
root.right = node_2
node_1.right = node_3

sol = Tree()
sol.traverseTree(root)