# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。 
# 
#  叶子节点 是指没有子节点的节点。 
# 
#  
#  
#  
#  
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1,2], targetSum = 0
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点总数在范围 [0, 5000] 内 
#  -1000 <= Node.val <= 1000 
#  -1000 <= targetSum <= 1000 
#  
# 
#  Related Topics 树 深度优先搜索 回溯 二叉树 👍 839 👎 0
import collections


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []
        if not root:
            return []

        parent = collections.defaultdict(lambda: None)
        # print("parent['hello'] = ", parent['hello'])
        # 我们使用哈希表记录树中的每一个节点的父节点。每次找到一个满足条件的节点，
        # 我们就从该节点出发不断向父节点迭代，即可还原出从根节点到当前节点的路径。

        def getPath(node: TreeNode):
            tmp = list()
            while node:
                tmp.append(node.val)
                node = parent[node]
            ret.append(tmp[::-1])

        que_node = collections.deque([root])
        que_total = collections.deque([0])

        while que_node:
            node = que_node.popleft()
            vec = que_total.popleft() + node.val
            if not node.left and not node.right:
                if vec == targetSum:
                    getPath(node)
            else:
                if node.left:
                    que_node.append(node.left)
                    parent[node.left] = node
                    que_total.append(vec)
                if node.right:
                    que_node.append(node.right)
                    parent[node.right] = node
                    que_total.append(vec)
        return ret
# leetcode submit region end(Prohibit modification and deletion)
