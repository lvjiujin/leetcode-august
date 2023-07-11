# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
#  
# 
#  示例 2: 
# 
#  
# 输入: [1,null,3]
# 输出: [1,3]
#  
# 
#  示例 3: 
# 
#  
# 输入: []
# 输出: []
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [0,100] 
#  
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 756 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 方法一：深度优先：
        # rightmost_value_at_depth = dict()  # 深度为索引，存放节点的值
        # max_depth = -1
        #
        # stack = [(root, 0)]
        # while stack:
        #     node, depth = stack.pop()
        #
        #     if node is not None:
        #         # 维护二叉树的最大深度
        #         max_depth = max(max_depth, depth)
        #
        #         # 如果不存在对应深度的节点我们才插入
        #         rightmost_value_at_depth.setdefault(depth, node.val)
        #
        #         stack.append((node.left, depth + 1))
        #         stack.append((node.right, depth + 1))
        #
        # return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]

        # 方法二：广度优先：二叉树的层序遍历: 获取每一层最右边的元素即可。
        if not root:
            return []
        import collections
        stack, res = collections.deque([root]), []

        while stack:
            size = len(stack)

            for i in range(size):
                r = stack.popleft()
                if i == size -1:
                    res.append(r.val)
                if r.left:
                    stack.append(r.left)
                if r.right:
                    stack.append(r.right)

        return res

        # 方法三：
        # rightmost_value_at_depth = dict()  # 深度为索引，存放节点的值
        # max_depth = -1
        #
        # queue = collections.deque([(root, 0)])
        # while queue:
        #     node, depth = queue.popleft()
        #
        #     if node is not None:
        #         # 维护二叉树的最大深度
        #         max_depth = max(max_depth, depth)
        #
        #         # 由于每一层最后一个访问到的节点才是我们要的答案，因此不断更新对应深度的信息即可
        #         rightmost_value_at_depth[depth] = node.val
        #
        #         queue.append((node.left, depth + 1))
        #         queue.append((node.right, depth + 1))
        #
        # return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]



# leetcode submit region end(Prohibit modification and deletion)
