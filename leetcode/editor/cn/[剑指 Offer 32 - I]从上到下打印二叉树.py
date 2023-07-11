# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。 
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
#  返回： 
# 
#  [3,9,20,15,7]
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
#  Related Topics 树 广度优先搜索 二叉树 👍 235 👎 0

import collections
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        # 二叉树的层序遍历
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur is not None:
                    res.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
        return res

# leetcode submit region end(Prohibit modification and deletion)
