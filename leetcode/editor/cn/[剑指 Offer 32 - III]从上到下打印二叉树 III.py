# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。 
# 
#  
# 
#  例如: 给定二叉树: [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 1000 
#  
# 
#  Related Topics 树 广度优先搜索 二叉树 👍 258 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []
        i = 0
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                cur = queue.popleft()
                if cur is not None:
                    temp.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
            if len(temp) > 0:
                if i % 2 == 0:
                    res.append(temp)
                else:
                    res.append(temp[::-1])
            i += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
