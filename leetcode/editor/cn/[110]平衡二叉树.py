# 给定一个二叉树，判断它是否是高度平衡的二叉树。 
# 
#  本题中，一棵高度平衡二叉树定义为： 
# 
#  
#  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：root = []
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数在范围 [0, 5000] 内 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 1140 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 方法一：从上到下：
        # 该方法存在部分重复，对于同一个节点，函数 depth 会被重复调用，导致时间复杂度较高
        # def depth(node: TreeNode):
        #     # 计算树中节点的深度
        #     if not node:
        #         return 0
        #     return max(depth(node.left), depth(node.right)) + 1
        # if not root:
        #     return True
        # # 分别计算左右子树的深度
        # left = depth(root.left)
        # right = depth(root.right)
        # # 这两个子树的深度不能超过1，并且他的两个子树也必须是平衡二叉树
        # return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        # 方法二：从下到上：（效率更好）
        def depth(node: TreeNode):
            if not node: # 当越过叶子节点，返回深度为0
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # left_depth , right_depth == -1，深度差大于1说明不是平衡二叉树，返回-1
            if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1
            else:
                return max(left_depth, right_depth) + 1
        return depth(root) >= 0


# leetcode submit region end(Prohibit modification and deletion)
