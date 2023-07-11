# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。 
# 
#  示例1： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4 
# 
#  限制： 
# 
#  0 <= 链表长度 <= 1000 
# 
#  注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/ 
# 
#  Related Topics 递归 链表 👍 291 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 用递归非常简单
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            merged_head = l1
            merged_head.next = self.mergeTwoLists(l1.next, l2)
        else:
            merged_head = l2
            merged_head.next = self.mergeTwoLists(l1, l2.next)

        return merged_head

# leetcode submit region end(Prohibit modification and deletion)
