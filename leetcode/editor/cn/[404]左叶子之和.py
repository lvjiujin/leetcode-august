# 给定二叉树的根节点 root ，返回所有左叶子之和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: root = [3,9,20,null,null,15,7] 
# 输出: 24 
# 解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
#  
# 
#  示例 2: 
# 
#  
# 输入: root = [1]
# 输出: 0
#  
# 
#  
# 
#  提示: 
# 
#  
#  节点数在 [1, 1000] 范围内 
#  -1000 <= Node.val <= 1000 
#  
# 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 501 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        isLeafNode = lambda node: not node.left and not node.right
        # 方法一 DFS（深度优先搜索）

        def dfs(node: TreeNode):
            ans = 0
            if node.left:
                ans += node.left.val if isLeafNode(node.left) else dfs(node.left)
            if node.right and not isLeafNode(node.right):
                ans += dfs(node.right)
            return ans
        return dfs(root) if root else 0

        # 方法二：BFS（广度优先搜索）
        # if not root:
        #     return 0
        # isLeafNode = lambda node: not node.left and not node.right
        # import collections
        # q = collections.deque([root])
        # res = 0
        # while q:
        #     node = q.popleft()
        #     if node.left:
        #         if isLeafNode(node.left):
        #             res += node.left.val
        #         else:
        #             q.append(node.left)
        #     if node.right:
        #         if not isLeafNode(node.right):
        #             q.append(node.right)
        #
        # return res
# leetcode submit region end(Prohibit modification and deletion)
