# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,null,2,3]
# 输出：[3,2,1]
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
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [0, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：递归算法很简单，你可以通过迭代算法完成吗？ 
# 
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 918 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 方法一：递归方法实现
        # res = []
        # def postorder(root: TreeNode):
        #     if not root:
        #         return
        #     postorder(root.left)
        #     postorder(root.right)
        #     res.append(root.val)
        #
        # postorder(root)
        # return res
        # 方法二：用栈来模拟反向输出

        # if not root:
        #     return []
        # stack, output = [root, ], []
        # while stack:
        #     node = stack.pop()
        #     output.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return output[::-1]
        # stack, output = [(0, root)], []
        # while stack:
        #     flag, node = stack.pop()
        #     if not node:
        #         continue
        #     if flag:
        #         output.append(node.val)
        #     else:
        #         stack.append((1, node))
        #         stack.append((0, node.right))
        #         stack.append((0, node.left))
        # return output
        #


# leetcode submit region end(Prohibit modification and deletion)
