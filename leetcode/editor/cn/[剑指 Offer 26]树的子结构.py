# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构) 
# 
#  B是A的子结构， 即 A中有出现和B相同的结构和节点值。 
# 
#  例如: 给定的树 A: 
# 
#  3 / \ 4 5 / \ 1 2 给定的树 B： 
# 
#  4 / 1 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。 
# 
#  示例 1： 
# 
#  输入：A = [1,2,3], B = [3,1]
# 输出：false
#  
# 
#  示例 2： 
# 
#  输入：A = [3,4,5,1,2], B = [4,1]
# 输出：true 
# 
#  限制： 
# 
#  0 <= 节点个数 <= 10000 
# 
#  Related Topics 树 深度优先搜索 二叉树 👍 652 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        result = False

        def DoesTree1HasTree2(root1, root2):
            # 这个顺序很关键。递归的终止条件是A树或B树到达叶子节点。
            if not root2:
                # 如果B树遍历完，说明找到了B树的子结构。
                return True
            if not root1:
                # A树遍历完，不能确定是否找到了B树的子结构，所以需要先将B树的判断放前面。
                return False

            if root1.val != root2.val:
                return False
            return DoesTree1HasTree2(root1.left, root2.left) \
                   and DoesTree1HasTree2(root1.right, root2.right)

        if A and B:
            # 第一步，先在A树中找到和B树中根节点一样的值R。
            if A.val == B.val:
                # 第二步: 判断以R为根节点的子树中是否含有和B一样的结构。
                result = DoesTree1HasTree2(A, B)
            if not result:
                result = self.isSubStructure(A.left, B)
            if not result:
                result = self.isSubStructure(A.right, B)
        # A，B只要有一个为空树，那么就不满足要求。题目要求空树不能成为子树。
        return result



# leetcode submit region end(Prohibit modification and deletion)
