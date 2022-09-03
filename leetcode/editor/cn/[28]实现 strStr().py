# 实现 strStr() 函数。 
# 
#  给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如
# 果不存在，则返回 -1 。 
# 
#  说明： 
# 
#  当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。 
# 
#  对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：haystack = "hello", needle = "ll"
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：haystack = "aaaaa", needle = "bba"
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= haystack.length, needle.length <= 10⁴ 
#  haystack 和 needle 仅由小写英文字符组成 
#  
# 
#  Related Topics 双指针 字符串 字符串匹配 👍 1573 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle:
            return -1
        # if needle not in haystack:
        #     return -1
        # # return haystack.index(needle)
        # has_lst = haystack.split(needle)[0]
        # return len(has_lst)
        # 暴力方法:
        # n, m = len(haystack), len(needle)
        # if n < m:
        #     return -1
        # for i in range(0, n - m +1, 1):
        #     if haystack[i:i+m] == needle:
        #         return i
        # return -1

        # 单纯的kmp算法
        n, m = len(haystack), len(needle)
        next = self.get_next(needle)
        print("next = ", next)
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j-1]
            if haystack[i] == needle[j]:
                j += 1
                if j == m:
                    return i -m +1
        return -1


    def get_next(self, p):
        m = len(p)
        next = [0 for _ in range(m)]
        left = 0
        for right in range(1, m):
            while left > 0 and p[left] != p[right]:
                left = next[left-1]
            if p[left] == p[right]:
                left += 1
            next[right] = left
        return next



# leetcode submit region end(Prohibit modification and deletion)
