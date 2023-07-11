# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。 
# 
#  假设二叉树中至少有一个节点。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: root = [2,1,3]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: [1,2,3,4,null,5,6,null,null,7]
# 输出: 7
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [1,10⁴] 
#  
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 384 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 层序遍历
        import collections
        # q = collections.deque([root])
        # output =[]
        # while q:
        #     size = len(q)
        #     vals = []
        #     for _ in range(size):
        #         node = q.popleft()
        #         vals.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     output.append(vals)
        #
        # return output[-1][0]
        # 方法二：BFS 广度优先，在遍历一个节点时，需要先把它的非空右子节点放入队列，
        # 然后再把它的非空左子节点放入队列，这样才能保证从右到左遍历每一层的节点。
        # 广度优先搜索所遍历的最后一个节点的值就是最底层最左边节点的值。

        # q = collections.deque([root])  # 这句代码等价于 q.append(root)
        # ans = 0
        # while q:
        #     node = q.popleft()
        #     if node.right:
        #         q.append(node.right)
        #     if node.left:
        #         q.append(node.left)
        #     ans = node.val
        # return ans
        # 方法三：
        # curVal = curHeight = 0
        #
        # def dfs(node: Optional[TreeNode], height: int) -> None:
        #     if not node:
        #         return
        #     height += 1
        #     dfs(node.left, height)
        #     dfs(node.right, height)
        #     nonlocal curVal, curHeight
        #     if height > curHeight:
        #         curHeight = height
        #         curVal = node.val
        #
        # dfs(root, 0)
        # return curVal
        # 方法四：
        queue = collections.deque()
        queue.append(root)
        bottomLeft = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:
                    bottomLeft = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return bottomLeft





# leetcode submit region end(Prohibit modification and deletion)
