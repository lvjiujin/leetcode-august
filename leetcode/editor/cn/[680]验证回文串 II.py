# 给你一个字符串 s，最多 可以从中删除一个字符。 
# 
#  请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aba"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abca"
# 输出：true
# 解释：你可以删除字符 'c' 。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "abc"
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 由小写英文字母组成 
#  
# 
#  Related Topics 贪心 双指针 字符串 👍 542 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        length = len(s)
        start = 0
        end = length - 1
        while start < length / 2 :
            if s[start] != s[end]:
                break
            start += 1
            end -= 1

        def isPalindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    break
                start += 1
                end -= 1
            return start >= end

        return (isPalindrome(s, start + 1, end)
                or isPalindrome(s, start, end - 1)
                or start == length / 2)



# leetcode submit region end(Prohibit modification and deletion)
