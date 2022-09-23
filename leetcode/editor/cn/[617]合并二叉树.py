# 给你两棵二叉树： root1 和 root2 。 
# 
#  想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠
# ，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 null 的节点将直接作为新二叉树的节点。 
# 
#  返回合并后的二叉树。 
# 
#  注意: 合并过程必须从两个树的根节点开始。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# 输出：[3,4,5,5,4,null,7]
#  
# 
#  示例 2： 
# 
#  
# 输入：root1 = [1], root2 = [1,2]
# 输出：[2,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  两棵树中的节点数目在范围 [0, 2000] 内 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1090 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root1 and not root2:
        #     return None
        # if not root1:
        #     return root2
        # if not root2:
        #     return root1
        # root = TreeNode(root1.val + root2.val)
        # root.left = self.mergeTrees(root1.left, root2.left)
        # root.right = self.mergeTrees(root1.right, root2.right)
        # return root

        if not root1:
            return root2
        if not root2:
            return root1
        import collections
        merged = TreeNode(root1.val + root2.val)
        queue = collections.deque([merged])
        queue1 = collections.deque([root1])
        queue2 = collections.deque([root2])

        while queue1 and queue2:
            node = queue.popleft()
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if left1 or left2:
                if left1 and left2:
                    left = TreeNode(left1.val + left2.val)
                    node.left = left
                    queue.append(left)
                    queue1.append(left1)
                    queue2.append(left2)
                elif left1:
                    node.left = left1
                elif left2:
                    node.left = left2
            if right1 or right2:
                if right1 and right2:
                    right = TreeNode(right1.val + right2.val)
                    node.right = right
                    queue.append(right)
                    queue1.append(right1)
                    queue2.append(right2)
                elif right1:
                    node.right = right1
                elif right2:
                    node.right = right2

        return merged


# leetcode submit region end(Prohibit modification and deletion)
