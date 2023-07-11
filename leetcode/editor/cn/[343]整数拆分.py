# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。 
# 
#  返回 你可以获得的最大乘积 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: n = 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。 
# 
#  示例 2: 
# 
#  
# 输入: n = 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。 
# 
#  
# 
#  提示: 
# 
#  
#  2 <= n <= 58 
#  
# 
#  Related Topics 数学 动态规划 👍 975 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        quotient, remainder = n // 3, n % 3
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2

    def integerBreak2(self, n: int) -> int:

        if n < 3:
            return n-1
        # 最基本的动态规划，解法。
        # dp[i]表示将正整数i拆分成至少两个正整数的和之后，这些正整数乘积的最大值。
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = max(2*(i-2), 2*dp[i-2], 3*(i-3), 3*dp[i-3])
        return dp[n]

    def integerBreak1(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        # 最基本的动态规划，解法。
        # dp[i]表示将正整数i拆分成至少两个正整数的和之后，这些正整数乘积的最大值。
        dp = [0] * (n + 1)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i-j])

        return dp[n]
# leetcode submit region end(Prohibit modification and deletion)
