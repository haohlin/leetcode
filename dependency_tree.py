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
    """
    遍历依赖树，对每个版本名保留深度小的版本号（版本仲裁），并计算每个版本的trail
    """
    queue = [root]      # 层序遍历队列
    level_rec = dict()  # 记录节点层数
    level_rec[root.name] = 0
    level = 0

    # BFS层序遍历
    while queue:
      size = len(queue)
      # 对一层所有节点遍历
      for i in range(size):
        root_i = queue.pop(0) # 父节点i
        curr_children = []    # 记录父节点i的有效子节点

        for child in root_i.children:       # 遍历父节点i的子节点
          if child.name not in level_rec:   # 如果不存在更浅层次的同名节点
            level_rec[child.name] = level   # 将此节点加入hashmap
            child.trail = root_i.trail + [root_i.name + ":" + root_i.version] # 此节点的trail = 父节点trail加上父节点
            queue.append(child)             # 将子节点加入队列
            curr_children.append(child)     # 将子节点加入有效子节点队列

        self.printInfo(root_i, curr_children) # print父节点i的信息
      level += 1 # 进入下一层

  def printInfo(self, node, curr_children):
    """
    输入：节点node和node的有效子节点
    输出：节点node的信息
    """
    print('name:' + node.name)
    print('version:' + node.version)
    children_list = []
    for child in curr_children:
      children_list.append(child.name + ":" + child.version)
    print('children: ' + str(children_list))
    print('trail:' + str(node.trail))
    print()

if __name__== "__main__":
  head = TreeNode(name='a', version='1.0')
  node1 = TreeNode(name='b', version='1.0')
  node2 = TreeNode(name='c', version='2.1')
  node3 = TreeNode(name='d', version='3.1')
  node4 = TreeNode(name='b', version='1.2')
  node5 = TreeNode(name='e', version='3.2')
  node6 = TreeNode(name='f', version='1.0')
  node7 = TreeNode(name='c', version='4.1')

  head.children = [node1, node3]
  node1.children = [node2]
  node3.children = [node4, node5]
  node4.children = [node6]
  node6.children = [node7]

  sol = Solution()
  sol.printTree(head)

"""
Test example:
        a:1.0
 b:1.0         d:3.1
     c:2.1 e:3.2  b:1.2
                f:1.0
              c:4.1
"""

"""
Test output:
name:a
version:1.0
children: ['b:1.0', 'd:3.1']
trail:[]

name:b
version:1.0
children: ['c:2.1']
trail:['a:1.0']

name:d
version:3.1
children: ['e:3.2']
trail:['a:1.0']

name:c
version:2.1
children: []
trail:['a:1.0', 'b:1.0']

name:e
version:3.2
children: []
trail:['a:1.0', 'd:3.1']

Explain:
b:1.2 与 上一层节点 b:1.0 冲突，保留 b:1.0 并删除 b:1.2 子树（b->f->c）
"""