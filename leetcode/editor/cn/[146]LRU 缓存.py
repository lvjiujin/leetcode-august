# 
#  请你设计并实现一个满足 
#  LRU (最近最少使用) 缓存 约束的数据结构。
#  
# 
#  
#  实现 
#  LRUCache 类：
#  
#
#  
#  
#  
#  LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存 
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 
#  void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 
# key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。 
#  
#  
#  
# 
#  函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。 
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 10000 
#  0 <= value <= 10⁵ 
#  最多调用 2 * 10⁵ 次 get 和 put 
#  
# 
#  Related Topics 设计 哈希表 链表 双向链表 👍 2430 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


class DLinkedNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode(-1, -1)
        self.tail = DLinkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # 将node移动都末尾:
        self.moveToTail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            # 更新node的值:
            node.value = value
            # 将node移动到末尾:
            self.moveToTail(node)

        else:
            # 只要满了就删。
            if len(self.cache) == self.capacity:
                # 删除最近最少使用的节点（头节点指向的节点)
                toBeDeletedNode = self.head.next

                self.deleteNode(toBeDeletedNode)
                # 删除哈希表中对应的项
                self.cache.pop(toBeDeletedNode.key)

            node = DLinkedNode(key, value)
            self.insertToTail(node)
            self.cache[key] = node

    def insertToTail(self, node: DLinkedNode):
        # 下面这四行代码顺序非常关键，顺序不能错。
        # 先让tail的前一个节点的next指针指向node.
        self.tail.prev.children = node
        # 在让node的prev指针指向tail的前一个节点.
        node.prev = self.tail.prev
        # node的next指针指向tail
        node.next = self.tail
        # tail的prev指针指向node.
        self.tail.prev = node

    def moveToTail(self, node: DLinkedNode):
        self.deleteNode(node)
        self.insertToTail(node)

    def deleteNode(self, node: DLinkedNode):
        node.prev.children = node.next
        node.next.prev = node.prev









# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
