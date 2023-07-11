# 两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。 
# 
#  给你两个整数 x 和 y，计算并返回它们之间的汉明距离。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 1, y = 4
# 输出：2
# 解释：
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# 上面的箭头指出了对应二进制位不同的位置。
#  
# 
#  示例 2： 
# 
#  
# 输入：x = 3, y = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= x, y <= 2³¹ - 1 
#  
# 
#  Related Topics 位运算 👍 655 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s1 = str(bin(x))[2:]
        s2 = str(bin(y))[2:]
        size1, size2 = len(s1), len(s2)
        if size1 < size2:
            s1 = '0' * (size2 - size1) + s1
        else:
            s2 = '0' * (size1 - size2) + s2

        diff = 0
        i = 0
        size = len(s1)
        while i < size :
            if s1[i] != s2[i]:
                diff += 1
            i+=1
        return diff


# leetcode submit region end(Prohibit modification and deletion)
