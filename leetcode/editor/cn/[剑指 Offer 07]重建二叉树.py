# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。 
# 
#  假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
# 
#  
# 
#  示例 1: 
#  
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 5000 
# 
#  
# 
#  注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/ 
# 
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 933 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(root, left, right):
            # 这里的root是先序遍历中的根节点索引。
            # 这里的left是中序遍历的左子树的第一个节点的索引。
            # 这里的right是中序遍历右子树的最后一个节点的索引
            if left > right:
                return  # 递归终止
            node = TreeNode(preorder[root])  # 建立根节点
            i = dic[preorder[root]]  # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)  # 开启左子树递归
            # i -left +root + 1:根节点索引+左子树长度+1， 即在先序遍历中找到右子树的根节点
            node.right = recur(i - left + root + 1, i + 1, right)  # 开启右子树递归
            return node  # 回溯返回根节点

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)

# leetcode submit region end(Prohibit modification and deletion)
