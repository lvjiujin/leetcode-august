# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 13
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 10⁹ 
#  
# 
#  Related Topics 递归 数学 动态规划 👍 477 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countDigitOne(self, n: int) -> int:
        mulk, k = 1, 0
        ans = 0
        while mulk <= n:
            ans += ((n // (mulk * 10)) * mulk + min(max(n % (mulk*10) - mulk + 1, 0), mulk))
            k += 1
            mulk *= 10

        return ans



# leetcode submit region end(Prohibit modification and deletion)
