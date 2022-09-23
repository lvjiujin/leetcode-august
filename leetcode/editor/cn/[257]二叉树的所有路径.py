# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。 
# 
#  叶子节点 是指没有子节点的节点。 
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1]
# 输出：["1"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [1, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics 树 深度优先搜索 字符串 回溯 二叉树 👍 820 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 方法1：dfs
        # paths = []
        #
        # def construct_paths(node, path):
        #     if node:
        #         path += str(node.val)
        #         if not node.left and not node.right:
        #             # 当前节点是叶子节点，则将路径加入到paths中
        #             paths.append(path)
        #         else:
        #             # 不是叶子节点，继续递归遍历
        #             path += '->'
        #             construct_paths(node.left, path)
        #             construct_paths(node.right, path)
        #
        # construct_paths(root, '')
        # return paths
        # 方法二：BFS，广度优先搜索
        paths = list()
        if not root:
            return paths
        import collections
        node_queue = collections.deque([root])
        path_queue = collections.deque([str(root.val)])

        while node_queue:
            node = node_queue.popleft()
            path = path_queue.popleft()

            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + '->' + str(node.left.val))

                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + '->' + str(node.right.val))
        return paths



# leetcode submit region end(Prohibit modification and deletion)
