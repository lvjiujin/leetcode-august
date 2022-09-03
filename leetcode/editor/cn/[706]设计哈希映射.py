# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。 
# 
#  实现 MyHashMap 类： 
# 
#  
#  MyHashMap() 用空映射初始化对象 
#  void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key 已经存在于映射中，
# 则更新其对应的值 value 。 
#  int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。 
#  void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# 输出：
# [null, null, null, 1, -1, null, 1, null, -1]
# 
# 解释：
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
# myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
# myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
# myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
# myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= key, value <= 10⁶ 
#  最多调用 10⁴ 次 put、get 和 remove 方法 
#  
# 
#  Related Topics 设计 数组 哈希表 链表 哈希函数 👍 320 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MyHashMap:
    # 方法一：利用dict，但是实际上不符合要求。
    # def __init__(self):
    #     self.hashmap = dict()
    #
    # def put(self, key: int, value: int) -> None:
    #     self.hashmap[key] = value
    #
    # def get(self, key: int) -> int:
    #     return self.hashmap.get(key, -1)
    #
    # def remove(self, key: int) -> None:
    #     if key in self.hashmap:
    #         self.hashmap.pop(key)

    # 方法二：利用一个大的列表，将key当成列表的下标，value当成列表中的元素。
    # def __init__(self):
    #     N = 10 ** 6+1
    #     self.data = [-1] * N
    #
    # def put(self, key: int, value: int) -> None:
    #     self.data[key] = value
    #
    # def get(self, key: int) -> int:
    #     if self.data[key] != -1:
    #         return self.data[key]
    #     return -1
    #
    # def remove(self, key: int) -> None:
    #     self.data[key] = -1

    def __init__(self):
        N = 10 ** 6+1
        self.data = [-1] * N

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        if self.data[key] != -1:
            return self.data[key]
        return -1

    def remove(self, key: int) -> None:
        self.data[key] = -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# leetcode submit region end(Prohibit modification and deletion)
