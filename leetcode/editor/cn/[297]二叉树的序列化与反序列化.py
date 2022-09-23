# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方
# 式重构得到原数据。 
# 
#  请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
# 反序列化为原始的树结构。 
# 
#  提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的
# 方法解决这个问题。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：[1]
#  
# 
#  示例 4： 
# 
#  
# 输入：root = [1,2]
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中结点数在范围 [0, 10⁴] 内 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 设计 字符串 二叉树 👍 978 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # 方法一：广度优先（相当于二叉树的层序遍历)
    # def serialize(self, root):
    #     """Encodes a tree to a single string.
    #
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     if not root:
    #         return ''
    #     from collections import deque
    #     q = deque()
    #     q.append(root)
    #     res = [str(root.val)]
    #
    #     while q:
    #         size = len(q)
    #         for _ in range(size):
    #             node = q.popleft()
    #             if node.left:
    #                 res.append(str(node.left.val))
    #                 q.append(node.left)
    #             else:
    #                 res.append('*')
    #             if node.right:
    #                 res.append(str(node.right.val))
    #                 q.append(node.right)
    #             else:
    #                 res.append('*')
    #     return ",".join(res)
    #
    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
    #
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     from collections import deque
    #     if not data:
    #         return None
    #     vals = data.split(',')
    #     root = TreeNode()
    #     root.val = int(vals[0])
    #     q = deque()
    #     q.append(root)
    #     idx = 0
    #     while q:
    #         for _ in range(len(q)):
    #             node = q.popleft()
    #             if vals[idx+1] != '*':
    #                 node.left = TreeNode()
    #                 node.left.val = int(vals[idx+1])
    #                 q.append(node.left)
    #
    #             if vals[idx+2] != "*":
    #                 node.right = TreeNode()
    #                 node.right.val = int(vals[idx+2])
    #                 q.append(node.right)
    #
    #             idx += 2
    #     return root

    # 方法二：深度优先DFS,这里一定要用递归，简单而且效率高。

    # def serialize(self, root):
    #     """Encodes a tree to a single string.
    #
    #    :type root: TreeNode
    #    :rtype: str
    #    """
    #
    #     def dfs(node):
    #         if node:
    #             vals.append(str(node.val))
    #             dfs(node.left)
    #             dfs(node.right)
    #         else:
    #             vals.append("#")
    #
    #     vals = []
    #     dfs(root)
    #     return ",".join(vals)
    #
    #
    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
    #
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #
    #     def dfs():
    #         v = next(vals)
    #         if v == "#":
    #             return None
    #         node = TreeNode(int(v))
    #         node.left = dfs()
    #         node.right = dfs()
    #         return node
    #
    #     vals = iter(data.split(","))
    #     return dfs()
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res.append(str(node.val))
            else:
                res.append("#")

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        parts = data.split(",")

        idx = 0
        val = parts[idx]

        if val == "#":
            return None

        root = TreeNode(int(val))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            idx += 1
            val = parts[idx]
            if val != "#":
                node.left = left = TreeNode(int(val))
                queue.append(left)
            idx += 1
            val = parts[idx]
            if val != "#":
                node.right = right = TreeNode(int(val))
                queue.append(right)
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
