# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。 
# 
#  
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
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
#  s.length <= 40000 
#  
# 
#  注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-
# repeating-characters/ 
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 506 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rk, ans = -1, 0 # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        n = len(s)
        occ = set()
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i-1])
            while rk + 1 < n and s[rk +1] not in occ:
                # 不断移动右指针
                occ.add(s[rk+1])
                rk += 1
            ans = max(ans, rk - i + 1)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
