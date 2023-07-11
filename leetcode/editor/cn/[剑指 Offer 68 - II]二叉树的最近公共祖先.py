# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。 
# 
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。” 
# 
#  例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4] 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#  
# 
#  示例 2: 
# 
#  输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#  
# 
#  
# 
#  说明: 
# 
#  
#  所有节点的值都是唯一的。 
#  p、q 为不同节点且均存在于给定的二叉树中。 
#  
# 
#  注意：本题与主站 236 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-
# a-binary-tree/ 
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 492 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __hash__(self):
        return hash((self.val, self.left, self.right))  # get a tuple's hash

    def __eq__(self, other):
        return (self.val, self.left, self.right) == (other.val, other.left, other.right)


class Solution:
    class Solution:

        def lowestCommonAncestor1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            # """
            # :type root: TreeNode
            # :type p: TreeNode
            # :type q: TreeNode
            # :rtype: TreeNode
            # """

            # Stack for tree traversal
            stack = [root]

            # Dictionary for parent pointers
            parent = {root: None}

            # Iterate until we find both the nodes p and q
            while p not in parent or q not in parent:

                node = stack.pop()

                # While traversing the tree, keep saving the parent pointers.
                if node.left:
                    parent[node.left] = node
                    stack.append(node.left)
                if node.right:
                    parent[node.right] = node
                    stack.append(node.right)

            # Ancestors set() for node p.
            ancestors = set()

            # Process all ancestors for node p using parent pointers.
            while p:
                ancestors.add(p)
                p = parent[p]

            # The first ancestor of q which appears in
            # p's ancestor set() is their lowest common ancestor.
            while q not in ancestors:
                q = parent[q]
            return q

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q



        
# leetcode submit region end(Prohibit modification and deletion)
