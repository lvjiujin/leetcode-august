# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。 
# 
#  
# 
#  示例 1: 
# 
#  给定二叉树 [3,9,20,null,null,15,7] 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回 true 。 示例 2: 
# 
#  给定二叉树 [1,2,2,3,3,null,null,4,4] 
# 
#  
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#  
# 
#  返回 false 。 
# 
#  
# 
#  限制： 
# 
#  
#  0 <= 树的结点个数 <= 10000 
#  
# 
#  注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/ 
# 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 320 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
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
