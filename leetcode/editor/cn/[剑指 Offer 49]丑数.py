# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。 
# 
#  
# 
#  示例: 
# 
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。 
# 
#  说明: 
# 
#  
#  1 是丑数。 
#  n 不超过1690。 
#  
# 
#  注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/ 
# 
#  Related Topics 哈希表 数学 动态规划 堆（优先队列） 👍 393 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0
        uglyData = [0 for _ in range(n)]
        uglyData[0] = 1
        ugly2, ugly3, ugly5 = 0, 0, 0
        nextUglyIndex = 1
        while nextUglyIndex < n:
            minUgly = min(uglyData[ugly2] * 2, uglyData[ugly3] * 3, uglyData[ugly5] * 5)
            uglyData[nextUglyIndex] = minUgly
            if uglyData[ugly2] * 2 <= uglyData[nextUglyIndex]:
                ugly2 += 1
            if uglyData[ugly3] * 3 <= uglyData[nextUglyIndex]:
                ugly3 += 1
            if uglyData[ugly5] * 5 <= uglyData[nextUglyIndex]:
                ugly5 += 1

            nextUglyIndex += 1
        return uglyData[n-1]
# leetcode submit region end(Prohibit modification and deletion)
