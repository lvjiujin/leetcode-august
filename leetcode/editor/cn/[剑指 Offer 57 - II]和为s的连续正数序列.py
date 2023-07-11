# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。 
# 
#  序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：target = 9
# 输出：[[2,3,4],[4,5]]
#  
# 
#  示例 2： 
# 
#  输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#
# 
#  
# 
#  限制： 
# 
#  
#  1 <= target <= 10^5 
#  
# 
#  
# 
#  Related Topics 数学 双指针 枚举 👍 489 👎 0
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 数学原理：
        result = collections.deque()
        for n in range(2, target//2 + 2):
            # 前n项和为target, 首项为a,根据等差数列的求和公式可以推出:
            a = (2 * target - n * (n - 1)) / (2 * n)
            if a <= 0:
                break
            if a == int(a):
                a = int(a)
                result.appendleft(list(range(a, a + n)))
        return list(result)

    def findContinuousSequence1(self, target: int) -> List[List[int]]:
        # 滑动窗口
        res = []
        j, seq_sum = 1, 0
        for i in range(1, target//2 + 2):
            seq_sum += i
            while seq_sum > target:
                seq_sum -= j
                j += 1
            if seq_sum == target:
                res.append(list(range(j, i+1)))

        return res





# leetcode submit region end(Prohibit modification and deletion)
