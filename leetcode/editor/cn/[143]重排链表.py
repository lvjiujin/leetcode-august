# 给定一个单链表 L 的头节点 head ，单链表 L 表示为： 
# 
#  
# L0 → L1 → … → Ln - 1 → Ln
#  
# 
#  请将其重新排列后变为： 
# 
#  
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → … 
# 
#  不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3] 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3] 
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 5 * 10⁴] 
#  1 <= node.val <= 1000 
#  
# 
#  Related Topics 栈 递归 链表 双指针 👍 1057 👎 0
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def link(node1: ListNode, node2: ListNode, head: ListNode):
            prev = head
            while node1 and node2:
                prev.children = node1
                temp = node1.next
                node1.next = node2
                prev = node2
                node2 = node2.children
                node1 = temp
            if node1:
                prev.children = node1

        def reverseList(head: Optional[ListNode]) -> ListNode:
            prev = None
            cur = head
            while cur is not None:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        dummy = ListNode(0)
        dummy.children = head
        slow = dummy
        fast = dummy
        while slow and fast.children:
            slow = slow.children
            fast = fast.children
            if fast.children:
                fast = fast.children
        temp = slow.children
        slow.children = None # 这个地方一定要特别小心，否则会出现环。
        link(head, reverseList(temp), dummy)


# leetcode submit region end(Prohibit modification and deletion)
