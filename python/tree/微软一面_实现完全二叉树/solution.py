# 完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。设计一个用完全二叉树初始化的数据结构 CBTInserter，
# 它支持以下几种操作：CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
# CBTInserter.insert(int v)  向树中插入一个新节点，节点类型为 TreeNode，值为 v 。使树保持完全二叉树的状态，并返回插入的新节点的父节点的值；
# CBTInserter.get_root() 将返回树的头节点。

# 示例 1：输入：inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
# 输出：[null,1,[1,2]]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:
    def __init__(self, root):
        self.arr = self.copyTree(root)
    
    def copyTree(self, root):
        queue = [root]
        result = []
        while queue:
            q_size = len(queue)
            result_i = []
            for i in range(q_size):
                cur_node = queue.pop(0)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                result_i.append(cur_node.val)
            result += result_i

        return result

    def insert(self, v):
        self.arr.append(v)
    
    def get_root(self):
        return self.arr[0]

"""
1
2 3
4

self.arr = [1,2,3,4]
"""
root = TreeNode(val=1)
node_1 = TreeNode(val=2)
node_2 = TreeNode(val=3)
node_3 = TreeNode(val=4)
root.left = node_1
root.right = node_2
node_1.left = node_3

tree_instance = CBTInserter(root)
print("Initial tree is: ", tree_instance.arr)

tree_instance.insert(5)
print("After insert is: ", tree_instance.arr)

print("Root is: ", tree_instance.get_root())