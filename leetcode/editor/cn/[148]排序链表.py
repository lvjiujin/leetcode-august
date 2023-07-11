# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 10⁴] 内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  
# 
#  进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
# 
#  Related Topics 链表 双指针 分治 排序 归并排序 👍 1806 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        def split(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            second = slow.next
            slow.next = None
            return second

        def merged(head1, head2):
            dummy = ListNode(0)
            cur = dummy
            while head1 and head2:
                if head1.val < head2.val:
                    cur.next = head1
                    head1 = head1.next
                else:
                    cur.next = head2
                    head2 = head2.next
                cur = cur.next
            cur.next = head2 if head2 else head1
            return dummy.next


        head1 = head
        head2 = split(head)
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        return merged(head1, head2)


# leetcode submit region end(Prohibit modification and deletion)
