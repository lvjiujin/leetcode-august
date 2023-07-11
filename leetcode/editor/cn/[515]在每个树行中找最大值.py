# 给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。 
# 
#  
# 
#  示例1： 
# 
#  
# 
#  
# 输入: root = [1,3,2,5,3,null,9]
# 输出: [1,3,9]
#  
# 
#  示例2： 
# 
#  
# 输入: root = [1,2,3]
# 输出: [1,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  二叉树的节点个数的范围是 [0,10⁴] 
#  
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 278 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        import collections
        deque = collections.deque()
        deque.append(root)
        ans = []
        while deque:
            length = len(deque)
            maxValue = deque[0].val
            for i in range(length):
                node = deque.popleft()
                if node.val > maxValue:
                    maxValue = node.val
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)

            ans.append(maxValue)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
