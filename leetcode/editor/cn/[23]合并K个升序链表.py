# 给你一个链表数组，每个链表都已经按升序排列。 
# 
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#  
# 
#  示例 2： 
# 
#  输入：lists = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  输入：lists = [[]]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  k == lists.length 
#  0 <= k <= 10^4 
#  0 <= lists[i].length <= 500 
#  -10^4 <= lists[i][j] <= 10^4 
#  lists[i] 按 升序 排列 
#  lists[i].length 的总和不超过 10^4 
#  
# 
#  Related Topics 链表 分治 堆（优先队列） 归并排序 👍 2210 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 最小堆的方法。

        # 为链表，则不能像数组一样排序,这个方法非常奇妙，一定要好好学习下。
        # 使用优先队列（最小堆），按照链表首位元素的大小排列
        if not lists:
            return None
        deque = []
        heapq.heapify(deque)
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(deque, (lists[i].val, i))
        head = ListNode()
        cur = head
        while deque:
            val, i = heapq.heappop(deque)
            cur.next = lists[i]
            lists[i] = lists[i].next
            cur = cur.next
            if lists[i]:
                heapq.heappush(deque, (lists[i].val, i))
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 方法二：归并法：
        if len(lists) == 0:
            return None

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
            cur.next = head1 if head1 else head2

            return dummy.next

        def mergeLists(lists, start, end):
            if start + 1 >= end:
                return lists[start]
            mid = (start + end) // 2
            head1 = mergeLists(lists, start, mid)
            head2 = mergeLists(lists, mid, end)
            return merged(head1, head2)

        return mergeLists(lists, 0, len(lists))

# leetcode submit region end(Prohibit modification and deletion)
