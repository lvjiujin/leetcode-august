# 给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。 
# 
#  如果树中有不止一个众数，可以按 任意顺序 返回。 
# 
#  假定 BST 满足如下定义： 
# 
#  
#  结点左子树中所含节点的值 小于等于 当前节点的值 
#  结点右子树中所含节点的值 大于等于 当前节点的值 
#  左子树和右子树都是二叉搜索树 
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,null,2,2]
# 输出：[2]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [1, 10⁴] 内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  
# 
#  进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内） 
# 
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 520 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # 方法一：递归：中序遍历非哈希

        # def inorder(node, lst):
        #     if not node:
        #         return None
        #     inorder(node.left, lst)
        #     lst.append(node.val)
        #     inorder(node.right, lst)
        # output = list()
        # inorder(root, output)
        #
        # prev = output[0]
        # count, max_count = 1, 1
        # res = [output[0]]
        # for x in output[1:]:
        #     if x == prev:
        #         count += 1
        #     else:
        #         count = 1
        #     if max_count == count:
        #         res.append(x)
        #
        #     if count > max_count:
        #
        #         max_count = count
        #         res = [x]
        #     prev = x
        # return res
        # 方法二：迭代法。
        stack = []
        pre = None  # 记录前一个元素值
        cnt = 0  # 记录次数
        maxCnt = 0  # 记录最大次数
        res = [] # 记录结果
        while root or stack:

            if root:
                stack.append(root)
                root = root.left  # 一直向左子树走，每一次将当前节点保存到栈中
            # 当前节点为空，证明走到了最左边，从栈中弹出节点
            # 开始对右子树重复上述过程
            else:
                cur = stack.pop()
                # 第一个节点
                if not pre:
                    cnt = 1
                # 如果与前一个节点的值相等
                elif pre.val == cur.val:
                    cnt += 1
                else:
                    cnt = 1
                # 如果和最大次数相同，将值放入 res
                if cnt == maxCnt:
                    res.append(cur.val)
                # 如果大于最大次数
                if cnt > maxCnt:
                    # 更新最大次数
                    maxCnt = cnt
                    # 重新更新 res
                    res = [cur.val]
                pre = cur
                root = cur.right
        return res





# leetcode submit region end(Prohibit modification and deletion)
