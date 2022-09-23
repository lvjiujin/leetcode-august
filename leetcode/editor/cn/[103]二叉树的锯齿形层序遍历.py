# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1]
# 输出：[[1]]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [0, 2000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 广度优先搜索 二叉树 👍 695 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 层序遍历，交替交换每一层的顺序。
        if not root:
            return []
        output, queue = [], [root]
        flag = False
        while queue:
            size = len(queue)
            flag = False if flag else True
            vals = []
            for _ in range(size):
                r = queue.pop(0)
                vals.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            if not flag:
                vals = vals[::-1]
            output.append(vals)
        return output


# leetcode submit region end(Prohibit modification and deletion)
