# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。 
# 
#  
# 
#  示例: 
# 
#  输入: a = 1, b = 1
# 输出: 2 
# 
#  
# 
#  提示： 
# 
#  
#  a, b 均可能是负数或 0 
#  结果不会溢出 32 位整数 
#  
# 
#  Related Topics 位运算 数学 👍 360 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def add(self, a: int, b: int) -> int:
        def bitAdd(a, b):  # 正数限定
            while b != 0:
                a, b = a ^ b, (a & b) << 1
            return a

        def reduce(a, b):  # 正数限定且a>=b
            while b != 0:
                a, b = a ^ b, ((a ^ b) & b) << 1
            return a

        if a * b >= 0:  # 正负相同
            if a >= 0 and b >= 0:
                return bitAdd(a, b)
            else:
                return -bitAdd(-a, -b)
        else:  # 一正一负
            if abs(a) < abs(b):  # 大数置前
                a, b = b, a
            if a < 0:
                return -reduce(-a, b)
            else:
                return reduce(a, -b)



# leetcode submit region end(Prohibit modification and deletion)
