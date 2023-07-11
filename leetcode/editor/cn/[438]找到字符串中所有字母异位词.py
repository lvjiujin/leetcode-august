# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。 
# 
#  异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, p.length <= 3 * 10⁴ 
#  s 和 p 仅包含小写字母 
#  
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 1023 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        res = []
        if m < n:
            return res
        cnt1 = [0 for _ in range(26)]
        cnt2 = [0 for _ in range(26)]
        for i in range(n):
            cnt1[ord(s[i]) - ord('a')] += 1
            cnt2[ord(p[i]) - ord('a')] += 1
        if cnt1 == cnt2:
            res.append(0)
        left = 0
        for right in range(n, m):
            cnt1[ord(s[left]) - ord('a')] -= 1
            cnt1[ord(s[right]) - ord('a')] += 1
            left += 1
            if cnt1 == cnt2:
                res.append(left)
        return res

# leetcode submit region end(Prohibit modification and deletion)
