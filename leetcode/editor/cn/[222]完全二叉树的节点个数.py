# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。 
# 
#  完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层
# 为第 h 层，则该层包含 1~ 2ʰ 个节点。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,4,5,6]
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目范围是[0, 5 * 10⁴] 
#  0 <= Node.val <= 5 * 10⁴ 
#  题目数据保证输入的树是 完全二叉树 
#  
# 
#  
# 
#  进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？ 
# 
#  Related Topics 树 深度优先搜索 二分查找 二叉树 👍 787 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 方法一：二叉树的层序遍历
        # if not root:
        #     return 0
        # from collections import deque
        # q = deque()
        # q.append(root)
        # count = 0
        # while q:
        #     # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数,不在同一层的就不会同时出现在队列中。
        #     size = len(q)
        #     # 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
        #     # 如果节点的左/右子树不为空，也放入队列中
        #     for _ in range(size):
        #         r = q.popleft()
        #         count += 1
        #         if r.left:
        #             q.append(r.left)
        #         if r.right:
        #             q.append(r.right)
        #     # 将临时list加入最终返回结果中
        #
        # return count
        # 方法二：简单的递归
        # if not root:
        #     return 0
        # left = self.countNodes(root.left)
        # right = self.countNodes(root.right)
        # return left + right + 1
        # 方法三：考虑完全二叉树的性质:
        if not root:
            return 0
        left = root.left
        right = root.right
        leftDepth = 0  # 这里初始为0是有目的的，为了下面求指数方便
        rightDepth = 0
        while left:  # 求左子树深度
            left = left.left
            leftDepth += 1
        while right:  # 求右子树深度
            right = right.right
            rightDepth += 1
        if leftDepth == rightDepth:
            return (2 << leftDepth) - 1  # 注意(2<<1) 相当于2^2，所以leftDepth初始为0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

# leetcode submit region end(Prohibit modification and deletion)
