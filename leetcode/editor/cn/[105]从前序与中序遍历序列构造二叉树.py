# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并
# 返回其根节点。 
# 
#  
# 
#  示例 1: 
#  
#  
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= preorder.length <= 3000 
#  inorder.length == preorder.length 
#  -3000 <= preorder[i], inorder[i] <= 3000 
#  preorder 和 inorder 均 无重复 元素 
#  inorder 均出现在 preorder 
#  preorder 保证 为二叉树的前序遍历序列 
#  inorder 保证 为二叉树的中序遍历序列 
#  
# 
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 1724 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) != len(inorder):
            return None

        # 方法一：递归法:
        # def createTree(sub_preorder, sub_inorder, n):
        #     if not n:
        #         return None
        #     k = 0
        #     while sub_preorder[0] != sub_inorder[k]:
        #         k += 1
        #     node = TreeNode(sub_inorder[k])
        #     # 因为左右子树可能元素个数不相同，实际上这里的参数分别给出了左右子树的个数。一遍每一次递归的时候进行分割。
        #     node.left = createTree(sub_preorder[1:k+1], sub_inorder[0:k], k)
        #     node.right = createTree(sub_preorder[k+1:], sub_inorder[k+1:], n - k -1)
        #
        #     return node
        # return createTree(preorder, inorder, len(preorder))
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.reverse()
        return build(None)

        # 方法二，采用hash映射来降低在中序遍历中查找根节点的复杂度.
        # if len(preorder) != len(inorder) or not preorder or not inorder:
        #     return None
        # inorder_map = {value: i for i, value in enumerate(inorder)}
        #
        # def create_tree(pre_left, pre_right, in_left, in_right):
        #     if pre_left > pre_right:
        #         return None
        #     pre_root = preorder[pre_left]
        #     in_root_index = inorder_map.get(pre_root)
        #     root = TreeNode(pre_root)
        #     in_left_size = in_root_index-in_left
        #
        #     root.left = create_tree(pre_left+1, pre_left + in_left_size, in_left, in_root_index -1)
        #     root.right = create_tree(pre_left + in_left_size + 1, pre_right, in_root_index+1, in_right)
        #
        #     return root
        # n = len(inorder)
        # root = create_tree(0, n-1, 0, n-1)
        # return root



        # 方法二：用栈的方法
        """
        如果使用栈来解决首先要搞懂一个知识点，就是前序遍历挨着的两个值比如m和n，他们会有下面两种情况之一的关系。

        1，n是m左子树节点的值。
         如果节点m的左子树不为空，那么n是m的左子树。
        2，n是m右子树节点的值或者是m某个祖先节点的右节点的值。
         如果节点m的左子树为空，那么n是m的右子树
         如果节点m的左右子树都为空，那么n是m某个公共祖先的右节点的值
         
         迭代法本质上是在模拟二叉树的遍历工作栈。

        前序序列对应节点入栈序列，中序序列对应节点第一次出栈序列（第二次出栈是后序遍历才需要的，
        前序中序迭代法可以直接略过这次出栈）。 迭代法中的index指向的元素是当前应该出栈元素，
        若指向元素不等于栈顶元素，说明还需要遍历左子树（即前序序列向前遍历）；若指向元素等于栈顶元素，
        说明左子树已遍历完全（即前序序列遍历完左子树部分），开始遍历栈顶元素的右子树。
        如此遍历一遍前序和中序序列，即可构建一颗二叉树。
        """
        # if not preorder or not inorder or len(preorder) != len(inorder):
        #     return None
        # # 先序遍历第一个值作为根节点
        # root = TreeNode(preorder[0])
        # stack = [root]
        # inorderIndex = 0
        # #
        # for i in range(1, len(preorder)):
        #     preorderVal = preorder[i]
        #     node = stack[-1]
        #     # 第一种情况
        #     if node.val != inorder[inorderIndex]:
        #         node.left = TreeNode(preorderVal)
        #         stack.append(node.left)
        #     else:  # 第二种情况
        #         while stack and stack[-1].val == inorder[inorderIndex]:
        #             node = stack.pop()
        #             inorderIndex += 1
        #         node.right = TreeNode(preorderVal)
        #         stack.append(node.right)
        #
        # return root

# leetcode submit region end(Prohibit modification and deletion)
