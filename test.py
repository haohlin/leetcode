
'''

有一个依赖树,以下英文字母表示依赖名称,:后是版本号.
要求以深度小的版本优先来进行版本仲裁,
如下图中最后仲裁后b的版本是1.0,而不是1.2.
        a:1.0
 b:1.0         d:3.1
     c:2.1 e:3.2  b:1.2
                f:1.0
              c:4.1
              


      a:1.0
 b:1.0      d:3.1
    c:2.1       b:1.2
            e:3.2

node:name,version,children,trail(c:2.1 = a:1.0/b:1.0, b:1.0=a:1.0 )

name:a
version:1.0
children:[ 
{name:b,version:1.0,children:[{name:c,version:2.1,children:null,trail:'b:1.0/a.:1.0'}],trail:'a:.1.0'},
{name:d,versino3.1,children:[{name:e}]}
]
trail:''

root.trail=[]
'''
class TreeNode:
    def __init__(self, name=None, version=None, children=[], trail=[]):
        self.name = name
        self.version = version
        self.children = children
        self.trail = trail

class Solution:
  def printTree(self, root):
    def DFS(root):
      if not root:
        return
      root.trail = trail_i.copy()
      trail_i.append(root.name + ":" + root.version)
      for child in root.children:
        DFS(child)
      trail_i.pop()
    
    trail_i = []
    DFS(root)

head = TreeNode(name='a', version='1.0')
node1 = TreeNode(name='b', version='1.0')
node2 = TreeNode(name='c', version='2.1')
node3 = TreeNode(name='d', version='3.1')
node4 = TreeNode(name='b', version='1.2')
node5 = TreeNode(name='e', version='3.2')

head.children = [node1, node3]
node1.children = [node2]
node3.children = [node4]
node4.children = [node5]

def printTrail(root):
    if not root:
        return
    print(root.name + "'s trail:")
    print(root.trail)
    for child in root.children:
        printTrail(child)
    return

sol = Solution()
res = sol.printTree(head)
printTrail(head)