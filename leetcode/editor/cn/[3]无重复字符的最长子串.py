# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s 由英文字母、数字、符号和空格组成 
#  
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 8087 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ss = ""
        res = []
        for x in s:
            if x not in ss:
                ss += x
                res.append(ss)

            else:

                index = ss.find(x)
                ss = ss[index+1:] + x

        return max([len(x) for x in res])
        # 滑动窗口法：
        # 当没有重复字符时调整右边界，有重复字符时调整左边界
        # if not s:
        #     return 0
        # freq = {}
        # start = max_length = 0
        # for end, c in enumerate(s):
        #     freq[c] = freq.get(c, 0) + 1
        #     while freq[c] > 1:
        #         freq[s[start]] -=1
        #         start+=1
        #     max_length = max(max_length, end-start + 1)
        # return max_length

# leetcode submit region end(Prohibit modification and deletion)
