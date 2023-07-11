# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指
# 向链表中的任意节点或者 null。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
#  
# 
#  示例 4： 
# 
#  输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
#  
# 
#  
# 
#  提示： 
# 
#  
#  -10000 <= Node.val <= 10000 
#  Node.random 为空（null）或指向链表中的节点。 
#  节点数目不超过 1000 。 
#  
# 
#  
# 
#  注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-
# pointer/ 
# 
#  
# 
#  Related Topics 哈希表 链表 👍 612 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy


class Solution:

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        # 复制所有节点，插入原节点的后面
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next, None)
            cur = cur.next.next

        # 连接所有复制的节点的random指针
        cur = head
        copyHead = head.next
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 断开原链表与复制链表之间的连接
        cur = head
        cur_ = copyHead
        while cur and cur_:
            cur.next = cur_.next
            cur = cur.next
            if cur:
                cur_.next = cur.next
            cur_ = cur_.next
        return copyHead

    def copyRandomList2(self, head: 'Node') -> 'Node':
        # 在Python中不能采用这种方法，因为Python中使用自定义类对象作为字典的key,需要：
        # 在自定义类中实现两个方法__hash__, __eq__.
        #    def __hash__(self):
        #         return hash(self.name + str(self.age))
        #
        #     def __eq__(self, other):
        #         if self.name == other.name and self.age == other.age:
        #             return True
        #         return False
        if not head:
            return head
        return copy.deepcopy(head)


        
# leetcode submit region end(Prohibit modification and deletion)
