# 评测题目: write a function to return the length of the longest consecutive sequence of a tree

class TreeNode:
  def __init__(self, val=0, children=[]):
    self.val = val
    self.children = children

class Solution:
    def longestConSeq(self, root):
      max_len = 0
      
      def dfs(root, cur_len):
        if not root:
          return
        next_len = 1
        for c in root.children:
            if root.val + 1 == c.val:
                next_len = cur_len + 1
            else:
                max_len = max(max_len, cur_len)
                next_len = 1              
            dfs(c, next_len)
        return 
      
      dfs(root, 1)
      return max_len
    