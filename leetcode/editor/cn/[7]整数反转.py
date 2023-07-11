# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。 
# 
#  如果反转后整数超过 32 位的有符号整数的范围 [−2³¹, 231 − 1] ，就返回 0。 
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 123
# 输出：321
#  
# 
#  示例 2： 
# 
#  
# 输入：x = -123
# 输出：-321
#  
# 
#  示例 3： 
# 
#  
# 输入：x = 120
# 输出：21
#  
# 
#  示例 4： 
# 
#  
# 输入：x = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
# 
#  Related Topics 数学 👍 3677 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse2(self, x: int) -> int:
        # 负数是不能进行求余操作的。
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        result,  y = 0, abs(x)
        while y != 0:
            temp = y % 10
            result = result * 10 + temp
            if result > boundry:
                return 0
            y //= 10

        return result if x > 0 else -result

    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        s = str(x)
        if x < 0:
            ss = "-" + s[:0:-1]
        else:
            ss = s[::-1]

        res = int(ss)
        if res > 2 ** 31 - 1 or res < -2**31:
            res = 0
        return res

# leetcode submit region end(Prohibit modification and deletion)
