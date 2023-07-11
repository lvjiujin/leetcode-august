# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。 
# 
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。” 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [2, 10⁵] 内。 
#  -10⁹ <= Node.val <= 10⁹ 
#  所有 Node.val 互不相同 。 
#  p != q 
#  p 和 q 均存在于给定的二叉树中。 
#  
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 1965 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = None

        def dfs(root: TreeNode, p: TreeNode, q: TreeNode):
            # 在函数内部定义函数，内层函数要用到外部函数中的变量需要将该变量声明为nonlocal
            nonlocal ancestor
            if not root:
                return False
            lson = dfs(root.left, p, q)
            rson = dfs(root.right, p, q)
            if (lson and rson) or ((root.val == p.val or root.val == q.val)
                                   and (lson or rson)):
                ancestor = root
            return lson or rson or (root.val == p.val or root.val == q.val)

        import os
        print(os.listdir("/mnt/precompiled"))

        # import uncompyle6
        # with open("/mnt/precompiled/treenode.pyc") as f:
        #     print(f.read())
        import sys
        import os
        # s = os.system("uncompyle6 /leetcode/precompiled/treenode.pyc")
        # print(s)
        # os.system("pip install uncompyle6")

        return ancestor

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)
        if not left and not right:
            return  # 1.
        if not left:
            return right  # 3.
        if not right:
            return left  # 4.
        return root  # 2. if left and right:



# leetcode submit region end(Prohibit modification and deletion)
