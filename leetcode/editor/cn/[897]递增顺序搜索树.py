# 给你一棵二叉搜索树的
#  root ，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [5,1,7]
# 输出：[1,null,5,null,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数的取值范围是 [1, 100] 
#  0 <= Node.val <= 1000 
#  
# 
#  Related Topics 栈 树 深度优先搜索 二叉搜索树 二叉树 👍 304 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # 中序遍历
        stack = []
        cur = root
        prev = None
        first = None

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            if prev is None:
                first = cur
            else:
                # 每遍历到一个节点要把前一个节点的指向右子节点的指针指向它。
                prev.right = cur

            prev = cur
            cur.left = None
            cur = cur.right
        return first


        
# leetcode submit region end(Prohibit modification and deletion)
