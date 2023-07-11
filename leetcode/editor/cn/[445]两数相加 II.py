# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。 
# 
#  你可以假设除了数字 0 之外，这两个数字都不会以零开头。 
# 
#  
# 
#  示例1： 
# 
#  
# 
#  
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
#  
# 
#  示例2： 
# 
#  
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
#  
# 
#  示例3： 
# 
#  
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表的长度范围为 [1, 100] 
#  0 <= node.val <= 9 
#  输入数据保证链表代表的数字无前导 0 
#  
# 
#  
# 
#  进阶：如果输入链表不能翻转该如何解决？ 
# 
#  Related Topics 栈 链表 数学 👍 557 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None:
                return None
            prev = None
            cur = head
            while cur is not None:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        lst1 = reverseList(l1)
        lst2 = reverseList(l2)
        carry = 0
        node = ListNode()
        head = node
        while lst1 or lst2:
            val1 = lst1.val if lst1 else 0
            val2 = lst2.val if lst2 else 0
            res = val1 + val2 + carry
            carry = 1 if res >= 10 else 0
            res = res - 10 if res >= 10 else res
            node.val = res

            if lst1 or lst2:
                tempNode = ListNode()
                node.children = tempNode
                node = node.children
            if lst1:
                lst1 = lst1.next
            if lst2:
                lst2 = lst2.next
        if carry == 1:
            temp = ListNode(1)
            node.children = temp

        reverseNode = reverseList(head)
        return reverseNode






# leetcode submit region end(Prohibit modification and deletion)
