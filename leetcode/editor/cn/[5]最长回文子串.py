# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
#
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 👍 5670 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 方法一：动态规划法
        # 在状态转移方程中，我们是从长度较短的字符串向长度较长的字符串进行转移的，因此一定要注意动态规划的循环顺序。
        # n = len(s)
        # if n < 2:
        #     return s
        # max_len = 1
        # begin = 0
        # # dp[i][j] 表示s[i..j]是否是回文
        # dp = [[False] * n for _ in range(n)]
        # # 对角线上肯定为True,即单个字符s[i]为回文
        # for i in range(n):
        #     dp[i][i] = False
        # # 对子串长度进行循环
        # for L in range(2, n+1):
        #     # 对子串开始位置进行循环
        #     for i in range(n):
        #         # 由子串长度和子串起始位置可以得到子串结束位置j = i + L -1
        #         j = i + L - 1
        #         if j >=n:
        #             break
        #         if s[i] != s[j]:
        #             dp[i][j] = False
        #         else:
        #             if j - i <3:
        #                 dp[i][j] = True
        #             else:
        #                 dp[i][j] = dp[i+1][j-1]
        #         # 只要dp[i][L] = True 成立，表示子串 s[i..L]是回文，此时记录回文长度和起始位置。
        #         if dp[i][j] and j - i + 1 > max_len:
        #             max_len = j - i + 1
        #             begin = i
        # return s[begin: begin + max_len]

        # 方法二：中心扩展法
        # start = end = 0
        # n = len(s)
        # for i in range(n):
        #     left1, right1 = self.expandAroundCenter(s, i, i)
        #     left2, right2 = self.expandAroundCenter(s, i, i+1)
        #     if right1 - left1 > end - start:
        #         start, end = left1, right1
        #     if right2 - left2 > end - start:
        #         start, end = left2, right2
        # return s[start:end+1]  # 回文肯定是头尾都包含的，所以这里end + 1
        # 方法三：manacher算法
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start + 1:end + 1:2]


    def expandAroundCenter(self, s, left, right):
        # 中心扩展法比动态规划法快多了。
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1

    # 方法三：马拉车算法.(manacher算法)

    def expand(self, s, left, right):
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left -2 ) //2















# leetcode submit region end(Prohibit modification and deletion)
