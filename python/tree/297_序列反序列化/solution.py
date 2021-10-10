# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"
        return ','.join([str(root.val), str(self.serialize(root.left)), str(self.serialize(root.right))])
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        return self.deserial_helper(data)
        
    def deserial_helper(self, data):
        if not data:
            return
        root_val = data.pop(0)
        if root_val == 'None':
            return None
        root = TreeNode(root_val)
        root.left = self.deserial_helper(data)
        root.right = self.deserial_helper(data)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))