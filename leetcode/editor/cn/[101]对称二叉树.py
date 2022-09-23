# 给你一个二叉树的根节点 root ， 检查它是否轴对称。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 1000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你可以运用递归和迭代两种方法解决这个问题吗？ 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 2113 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def search(left, right):
            if left is None and right is None:
                return True
            elif left is None and right is not None:
                return False
            elif right is None and left is not None:
                return False
            else:
                if left.val != right.val:
                    return False
                else:
                    return search(left.left, right.right) and search(left.right, right.left)
        return search(root, root)
        # 方法一：递归
        # def check(p: TreeNode, q:TreeNode):
        #     if not p and not q:
        #         return True
        #     if not p or not q:
        #         return False
        #     return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
        #
        # return check(root, root)
        # 方法二：迭代法（思路还是方法一的思路）

        # queue = [root, root]
        # while queue:
        #     left = queue.pop()
        #     right = queue.pop()
        #
        #     if not left and not right:
        #         continue
        #     if (not left or not right) or (left.val != right.val):
        #         return False
        #     queue.append(left.left)
        #     queue.append(right.right)
        #     queue.append(left.right)
        #     queue.append(right.left)
        # return True
        # 方法三：层序遍历：比对每一层结果是否对称，
        # 注意空结点一定要用null补充，方便比对，下一层就不需要在null结点继续拓展了
        queue = [root]
        while queue:
            size = len(queue)
            vals = []
            for _ in range(size):
                r = queue.pop(0)
                vals.append(r.val) # 注意这一语句放在判断前面而不是里面
                if r.val != 'null':
                    queue.append(r.left if r.left else TreeNode('null'))
                    queue.append(r.right if r.right else TreeNode('null'))

            if vals != vals[::-1]:
                return False
        return True





# leetcode submit region end(Prohibit modification and deletion)
