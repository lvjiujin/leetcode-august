# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并
# 返回这颗 二叉树 。 
# 
#  
# 
#  示例 1: 
#  
#  
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= inorder.length <= 3000 
#  postorder.length == inorder.length 
#  -3000 <= inorder[i], postorder[i] <= 3000 
#  inorder 和 postorder 都由 不同 的值组成 
#  postorder 中每一个值都在 inorder 中 
#  inorder 保证是树的中序遍历 
#  postorder 保证是树的后序遍历 
#  
# 
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 839 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None
        # def create_tree(sub_inorder, sub_postorder, n):
        #     if not n:
        #         return None
        #     k = 0
        #     while sub_inorder[k] != sub_postorder[-1]:
        #         k += 1
        #     node = TreeNode(sub_inorder[k])
        #     node.left = create_tree(sub_inorder[0:k], sub_postorder[0:k], k)
        #     node.right = create_tree(sub_inorder[k+1:], sub_postorder[k:-1], n-k-1)
        #     return node
        # return create_tree(inorder, postorder, len(postorder))
        # def build(stop):
        #     if inorder and inorder[-1] != stop:
        #         root = TreeNode(postorder.pop())
        #         root.left = build(root.val)
        #         inorder.pop()
        #         root.right = build(stop)
        #         return root
        #
        # # postorder.reverse()
        # inorder.reverse()
        # return build(None)

        # def makeTree(postorder, inorder):
        #     idx = {}
        #     for i, val in enumerate(inorder):
        #         idx[val] = i
        #
        #     stack = []
        #     head = None
        #     for val in postorder[::-1]:
        #         if not head:
        #             head = TreeNode(val)
        #             stack.append(head)
        #         else:
        #             node = TreeNode(val)
        #             if idx[val] > idx[stack[-1].val]:
        #                 stack[-1].right = node
        #             else:
        #                 while stack and idx[stack[-1].val] > idx[val]:
        #                     u = stack.pop()
        #                 u.left = node
        #             stack.append(node)
        #     return head
        #
        # return makeTree(postorder, inorder)

        # if not inorder or not postorder:
        #     return None
        # root = TreeNode(postorder[-1])
        # mid = inorder.index(postorder[-1])
        # root.left = self.buildTree(inorder[:mid], postorder[:mid])
        # root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])
        # return root
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def dfs(start, end):
            if start > end: return None
            root = TreeNode(postorder.pop())
            root_index = inorder_map[root.val]
            root.right = dfs(root_index + 1,
                             end)  # have to put right before left because postorder.pop will return the right node first
            root.left = dfs(start, root_index - 1)
            return root

        return dfs(0, len(inorder) - 1)
# leetcode submit region end(Prohibit modification and deletion)
