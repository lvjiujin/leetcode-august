# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
# 请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18
# 。 
# 
#  示例 1： 
# 
#  输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1 
# 
#  示例 2: 
# 
#  输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36 
# 
#  提示： 
# 
#  
#  2 <= n <= 58 
#  
# 
#  注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/ 
# 
#  Related Topics 数学 动态规划 👍 523 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def cuttingRope(self, n: int) -> int:
        if n <=3:
            return n-1
        quotient, reminder = n //3, n % 3
        if reminder == 0:
            return 3 ** quotient
        elif reminder == 1:
            return 3 ** (quotient -1) * 4
        else:
            return 3 ** quotient * 2

    def cuttingRope2(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        timesOf3 = n // 3
        if n - timesOf3 * 3 == 1:
            timesOf3 -= 1

        timesOf2 = (n -timesOf3 * 3)//2
        return 3 ** timesOf3 * (2 ** timesOf2)



# leetcode submit region end(Prohibit modification and deletion)
