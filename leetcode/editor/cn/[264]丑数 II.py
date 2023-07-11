# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。 
# 
#  丑数 就是只包含质因数 2、3 和/或 5 的正整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 1690 
#  
# 
#  Related Topics 哈希表 数学 动态规划 堆（优先队列） 👍 996 👎 0
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 最小堆
        factors = [2, 3, 5]
        heap = [1]
        seen = {1}
        for i in range(n - 1):
            # 每次取出堆顶最小元素x, 下次依次将不重复（哈希表去重) 的2x,3x,5x加入到堆中
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := factor * curr) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)

    def nthUglyNumber2(self, n: int) -> int:
        # 动态规划法
        uglyData = [0 for _ in range(n)]
        uglyData[0] = 1
        ugly2, ugly3, ugly5 = 0, 0, 0
        nextUglyIndex = 1
        while nextUglyIndex < n:
            minData = min(uglyData[ugly2] * 2, uglyData[ugly3] * 3, uglyData[ugly5] * 5)
            uglyData[nextUglyIndex] = minData
            if uglyData[ugly2] * 2 == uglyData[nextUglyIndex]:
                ugly2 += 1
            if uglyData[ugly3] * 3 == uglyData[nextUglyIndex]:
                ugly3 += 1
            if uglyData[ugly5] * 5 == uglyData[nextUglyIndex]:
                ugly5 += 1
            nextUglyIndex += 1
        return uglyData[n - 1]
# leetcode submit region end(Prohibit modification and deletion)
