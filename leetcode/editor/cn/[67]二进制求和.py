# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入:a = "11", b = "1"
# 输出："100" 
# 
#  示例 2： 
# 
#  
# 输入：a = "1010", b = "1011"
# 输出："10101" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= a.length, b.length <= 10⁴ 
#  a 和 b 仅由字符 '0' 或 '1' 组成 
#  字符串如果不是 "0" ，就不含前导零 
#  
# 
#  Related Topics 位运算 数学 字符串 模拟 👍 885 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            i -= 1
            j -= 1
            res = digit_a + digit_b + carry
            carry = 1 if res >= 2 else 0
            res = res - 2 if res >= 2 else res
            result.append(str(res))
        if carry == 1:
            result.append('1')

        return "".join(result[::-1])




# leetcode submit region end(Prohibit modification and deletion)
