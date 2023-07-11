# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。 
# 
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 
# 
#  1 / \ 2 2 / \ / \ 3 4 4 3 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的: 
# 
#  1 / \ 2 2 \ \ 3 3 
# 
#  
# 
#  示例 1： 
# 
#  输入：root = [1,2,2,3,4,4,3]
# 输出：true
#  
# 
#  示例 2： 
# 
#  输入：root = [1,2,2,null,3,null,3]
# 输出：false 
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 1000 
# 
#  注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/ 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 391 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:

        def search(left, right):
            if left is None and right is None:
                return True
            elif left and not right:
                return False
            elif right and not left:
                return False
            else:
                if left.val != right.val:
                    return False

                return search(left.right, right.left) and search(left.left, right.right)

        return search(root, root)

    def isSymmetric2(self, root: TreeNode) -> bool:
        import collections
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            if size > 1 and size % 2 == 1:
                return False
            vals = []
            for _ in range(size):
                r = queue.popleft()
                if r:
                    vals.append(r.val)  # 注意这一语句放在判断前面而不是里面
                    if r.val != 'null':
                        queue.append(r.left if r.left else TreeNode('null'))
                        queue.append(r.right if r.right else TreeNode('null'))

            if vals != vals[::-1]:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
