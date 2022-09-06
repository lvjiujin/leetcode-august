# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。 
# 
#  注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: num1 = "2", num2 = "3"
# 输出: "6" 
# 
#  示例 2: 
# 
#  
# 输入: num1 = "123", num2 = "456"
# 输出: "56088" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num1.length, num2.length <= 200 
#  num1 和 num2 只能由数字组成。 
#  num1 和 num2 都不包含任何前导零，除了数字0本身。 
#  
# 
#  Related Topics 数学 字符串 模拟 👍 1048 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        # 方法一：
        # ans = "0"
        # m, n = len(num1), len(num2)
        # for i in range(n - 1, -1, -1): # 对除数的每一位进行循环
        #     add = 0
        #     y = int(num2[i])
        #     curr = ["0"] * (n - i - 1)   # 这里就是为了除最低位以外，其余位相乘的结果补0.
        #     for j in range(m - 1, -1, -1):  # 对被除数的每一位进行循环。
        #         product = int(num1[j]) * y + add
        #         curr.append(str(product % 10))
        #         add = product // 10
        #     if add > 0:
        #         curr.append(str(add))
        #     curr = "".join(curr[::-1])
        #     ans = self.addStrings(ans, curr)  # 将每次相乘的结果相加。
        #
        # return ans

        # 方法二：
        m, n = len(num1), len(num2)
        ans = [0] * (m + n)
        for i in range(m-1, -1, -1):
            x = int(num1[i])
            for j in range(n-1, -1, -1):
                product = int(num2[j]) * x
                ans[i + j + 1] += product  # 这行代码神操作，非常厉害。
        for i in range(m+n-1, 0, -1):
            ans[i-1] += ans[i] // 10
            ans[i] %= 10
        index = 1 if ans[0] == 0 else 0
        return "".join([str(x) for x in ans[index:]])

    def addStrings(self, num1: str, num2: str) -> str:

        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        ans = []
        while i >= 0 or j >= 0 or carry != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result = x + y + carry
            ans.append(str(result % 10))
            carry = result // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])

# leetcode submit region end(Prohibit modification and deletion)
