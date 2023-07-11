# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数
# 值排序之后中间两个数的平均值。 
# 
#  例如， 
# 
#  [2,3,4] 的中位数是 3 
# 
#  [2,3] 的中位数是 (2 + 3) / 2 = 2.5 
# 
#  设计一个支持以下两种操作的数据结构： 
# 
#  
#  void addNum(int num) - 从数据流中添加一个整数到数据结构中。 
#  double findMedian() - 返回目前所有元素的中位数。 
#  
# 
#  示例 1： 
# 
#  输入：
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
# [[],[1],[2],[],[3],[]]
# 输出：[null,null,null,1.50000,null,2.00000]
#  
# 
#  示例 2： 
# 
#  输入：
# ["MedianFinder","addNum","findMedian","addNum","findMedian"]
# [[],[2],[],[3],[]]
# 输出：[null,null,2.00000,null,2.50000] 
# 
#  
# 
#  限制： 
# 
#  
#  最多会对 addNum、findMedian 进行 50000 次调用。 
#  
# 
#  注意：本题与主站 295 题相同：https://leetcode-cn.com/problems/find-median-from-data-
# stream/ 
# 
#  Related Topics 设计 双指针 数据流 排序 堆（优先队列） 👍 375 👎 0


from sortedcontainers import SortedList
import heapq

# leetcode submit region begin(Prohibit modification and deletion)


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.L_maxHeap = []  #左侧比右侧多1个，或者相同
        self.R_minHeap = []

    def addNum(self, num: int) -> None:
        # heapq.heappushpop(heap, item)
        # Push item on the heap, then pop and return the smallest item from the heap
        if len(self.L_maxHeap) == len(self.R_minHeap):
            heapq.heappush(self.L_maxHeap, -1 * heapq.heappushpop(self.R_minHeap, num))
        else:
            heapq.heappush(self.R_minHeap, -1 * heapq.heappushpop(self.L_maxHeap, -num))

    def findMedian(self) -> float:
        if len(self.L_maxHeap) == len(self.R_minHeap):
            res = (-1 * self.L_maxHeap[0] + self.R_minHeap[0]) / 2
        else:
            res = -1 * self.L_maxHeap[0]     #左侧多1位
        return res


class MedianFinder2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = SortedList()

    def addNum(self, num: int) -> None:
        self.lst.add(num)

    def findMedian(self) -> float:
        n = len(self.lst)
        return self.lst[n//2] if n % 2 == 1 else (self.lst[n//2] + self.lst[(n-1)//2])/2





# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)
