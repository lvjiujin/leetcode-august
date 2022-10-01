# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。 
# 
#  差值是一个正数，其数值等于两值之差的绝对值。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [4,2,6,1,3]
# 输出：1
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目范围是 [2, 10⁴] 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  
# 
#  注意：本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-
# nodes/ 相同 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉搜索树 二叉树 👍 375 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        # 中序遍历相邻元素的差值最小
        # 非递归的中序遍历:
        # stack, output = [], []
        # cur = root
        #
        # while stack or cur:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     node = stack.pop()
        #     # output.append(node.val)
        #
        #     if node.right:
        #         cur = node.right
        #
        # res = []
        # for i in range(0, len(output)-1):
        #     ans = abs(output[i] - output[i+1])
        #     res.append(ans)
        # return min(res)
        # 方法二
        # stack = []
        # p = root
        # pre = float('-inf')
        # min_val = float('inf')
        # while p or stack:
        #     while p:
        #         stack.append(p)
        #         p = p.left
        #     p = stack.pop()
        #     cur = p.val
        #     # 因为中序遍历是升序，所以后面减去前面永远不会出现负数，所以不用取绝对值
        #     if cur - pre < min_val:
        #         min_val = cur - pre
        #
        #     pre = cur
        #     p = p.right  # 注意，这个地方千万不能用if p.right: p = p.right. 这样容易形成死循环。
        #             # 最好pop()出来的换一个变量名。
        # return min_val

        stack = []
        p = root
        prev = float('-inf')
        min_val = float('inf')
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            node = stack.pop() # 注意pop出来后，换一个节点名称，不要再用p了。
            cur = node.val
            if cur - prev < min_val:
                min_val = cur - prev
            prev = cur
            if node.right:
                p = node.right

        return min_val






# leetcode submit region end(Prohibit modification and deletion)
