# 给你二叉树的根结点 root ，请你将它展开为一个单链表： 
# 
#  
#  展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。 
#  展开后的单链表应该与二叉树 先序遍历 顺序相同。 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
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
# 输入：root = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中结点数在范围 [0, 2000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？ 
# 
#  Related Topics 栈 树 深度优先搜索 链表 二叉树 👍 1302 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorder_lst = []
        # def preorderTraversal(root: TreeNode):
        #     if root:
        #         preorder_lst.append(root)
        #         preorderTraversal(root.left)
        #         preorderTraversal(root.right)
        # 先序遍历。
        # def preorderTraversal(root):
        #     stack = []
        #     node = root
        #     while node or stack:
        #         while node:
        #             preorder_lst.append(node)
        #             stack.append(node)
        #             node = node.left
        #         node = stack.pop()
        #         # print("node = ", node)
        #         node = node.right
        #
        # preorderTraversal(root)
        # size = len(preorder_lst)
        # for i in range(1, size):
        #     prev, curr = preorder_lst[i-1], preorder_lst[i]
        #     prev.left = None
        #     prev.right = curr
        # 方法二：前序遍历+ 同步展开
        if not root:
            return
        stack = [root]
        prev = None
        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            # 将 curr 赋值给 prev，进入下一个节点的访问，直到遍历结束
            prev = curr



# leetcode submit region end(Prohibit modification and deletion)
