# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。 
# 
#  
# 
#  示例 1： 
# 
#  输入: n = 3
# 输出: 6
#  
# 
#  示例 2： 
# 
#  输入: n = 9
# 输出: 45
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= n <= 10000 
#  
# 
#  Related Topics 位运算 递归 脑筋急转弯 👍 548 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumNums1(self, n: int) -> int:
        return sum(range(n+1))

    def sumNums2(self, n: int) -> int:
        # 下面这种递归不可以，因为不能使用if else 语句。
        return 0 if n == 0 else n + self.sumNums(n-1)

    def sumNums3(self, n: int) -> int:
        # 俄罗斯农民乘法: 被乘数/2, 乘数*2, 如果被乘数%2 == 1，则结果加上乘数
        multiplicand = n + 1  # 被乘数
        multiplier = n  # 乘数
        result = 0
        while multiplicand:
            if multiplicand & 1:
                result += multiplier
            multiplier <<= 1
            multiplicand >>= 1
        result >>= 1
        return result

    def sumNums(self, n: int) -> int:
        return (n ** 2 + n ) >> 1




# leetcode submit region end(Prohibit modification and deletion)
