# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [2,1,3]
# 输出：[2,3,1]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目范围在 [0, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1409 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root:
        #     return None
        # # 将当前节点的左右子树交换
        # root.left, root.right = root.right, root.left
        # # 递归交换当前节点的左子树和右子树
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        #
        # return root
        # 方法二：
        if not root:
            return None
            # 将二叉树中的节点逐层放入队列中，再迭代处理队列中的元素
        from collections import deque
        queue = deque([root])
        while queue:
            # 每次都从队列中拿一个节点，并交换这个节点的左右子树
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            # 如果当前节点的左子树不为空，则放入队列等待后续处理
            if node.left:
                queue.append(node.left)
            # 如果当前节点的右子树不为空，则放入队列等待后续处理
            if node.right:
                queue.append(node.right)
        # 返回处理完的根节点
        return root

# leetcode submit region end(Prohibit modification and deletion)
