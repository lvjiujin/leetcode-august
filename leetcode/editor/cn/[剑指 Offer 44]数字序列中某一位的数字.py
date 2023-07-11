# 数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，
# 等等。 
# 
#  请写一个函数，求任意第n位对应的数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 3
# 输出：3
#  
# 
#  示例 2： 
# 
#  输入：n = 11
# 输出：0 
# 
#  
# 
#  限制： 
# 
#  
#  0 <= n < 2^31 
#  
# 
#  注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/ 
# 
#  Related Topics 数学 二分查找 👍 296 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNthDigit(self, n: int) -> int:
        d, count = 1, 9
        while n > d * count:
            n -= d * count
            d += 1
            count *= 10
        index = n - 1
        start = 10 ** (d - 1)
        num = start + index // d
        digitIndex = index % d
        return num // 10 ** (d - digitIndex - 1) % 10


# leetcode submit region end(Prohibit modification and deletion)
