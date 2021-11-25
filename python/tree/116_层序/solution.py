# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        if not root: 
            return root
        q = [root]
        while q:
            prev_node = q[0]
            cur_node = prev_node
            q_size = len(q)
            for i in range(q_size):
                cur_node = q.pop(0)
                if i != 0:
                    prev_node.next = cur_node
                prev_node = cur_node
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            cur_node.next = None
        return root


class Solution2:
    # No extra space used
    def connect(self, root: 'Node') -> 'Node':
        if not root: 
            return root
        self.connectNeighbor(root.left, root.right)
        return root
    def connectNeighbor(self, node1, node2):
        if not node1 or not node2:
            return
        node1.next = node2
        self.connectNeighbor(node1.left, node1.right)
        self.connectNeighbor(node1.right, node2.left)
        self.connectNeighbor(node2.left, node2.right)
        return