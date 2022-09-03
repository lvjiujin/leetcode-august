# 给定一个非空的字符串
#  s ，检查是否可以通过由它的一个子串重复多次构成。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abab"
# 输出: true
# 解释: 可由子串 "ab" 重复两次构成。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "aba"
# 输出: false
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "abcabcabcabc"
# 输出: true
# 解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)
#  
# 
#  
# 
#  提示： 
# 
#  
#  
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 由小写英文字母组成 
#  
# 
#  Related Topics 字符串 字符串匹配 👍 769 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # if not s :
        #     return False
        # ss = s + s
        # return s in ss[1:-1]
        # 方法二:KMP算法.
        next = self.get_next(s)
        n, value = len(next), next[-1]
        if value > 0 and value % (n - value) == 0:
            return True
        else:
            return False


    def get_next(self, p):
        # get_next是统计出每个位置之前的子串的前后缀数目
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
