# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,2,1]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [1,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围[1, 10⁵] 内 
#  0 <= Node.val <= 9 
#  
# 
#  
# 
#  进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
# 
#  Related Topics 栈 递归 链表 双指针 👍 1537 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head.next
        while fast.children and fast.children.children:
            fast = fast.children.children
            slow = slow.next
        halfSecond = slow.next
        if fast.children:
            halfSecond = slow.next.children
        slow.next = None


        def equals(head1: Optional[ListNode], head2: Optional[ListNode]) -> bool:
            if head1 is None and head2 is None:
                return True
            node1 = head1
            node2 = head2
            while(node1 and node2):
                if node1.val != node2.val:
                    return False
                node1 = node1.children
                node2 = node2.children

            if node1 is None and node2 is None:
                return True

        def reverseList(head:Optional[ListNode]) -> Optional[ListNode]:
            if head is None or head.next is None:
                return head
            prev = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        temp = reverseList(halfSecond)
        return equals(head, temp)
