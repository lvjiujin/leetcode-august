# 给定一个二叉树，找出其最大深度。 
# 
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例： 给定二叉树 [3,9,20,null,null,15,7]， 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最大深度 3 。 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1364 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 方法一：递归法:
        # if not root:
        #     return 0
        #
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        # 方法二：广度优先:
        if not root:
            return 0
        max_dep = 0
        queue = [root]
        while queue:
            max_dep += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return max_dep



# leetcode submit region end(Prohibit modification and deletion)
