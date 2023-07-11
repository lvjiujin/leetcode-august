# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。 
# 
#  
#  '.' 匹配任意单个字符 
#  '*' 匹配零个或多个前面的那一个元素 
#  
# 
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。 
# 
#  示例 1： 
# 
#  
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 20 
#  1 <= p.length <= 30 
#  s 只包含从 a-z 的小写字母。 
#  p 只包含从 a-z 的小写字母，以及字符 . 和 *。 
#  保证每次出现字符 * 时，前面都匹配到有效的字符 
#  
# 
#  Related Topics 递归 字符串 动态规划 👍 3308 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isMatch(self, s: str, p: str) ->bool:
        map = dict()
        m, n = len(s), len(p)

        def dp(i, j):
            if j == n:
                return i == m
            if i == m:
                if (n - j) % 2 == 1:
                    return False
                while j+1 < n:
                    if p[j+1] != '*':
                        return False
                    j+=2
                return True
            key = str(i) + ',' + str(j)
            if key in map:
                return map[key]
            if s[i] == p[j] or p[j] == '.':
                if j + 1 < n and p[j+1] == '*':
                    res = dp(i, j+2) or dp(i+1, j)
                else:
                    res = dp(i+1, j+1)
            else:
                if j + 1 < n and p[j+1] == '*':
                    res = dp(i, j+2)
                else:
                    res = False
            map[key] = res
            return res

        return dp(0, 0)

    def isMatch2(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                # 当s为空串时，而p不需要匹配空串的时候，dp[i][j]就为False
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]
        # dp[i][j] 表示 s 的前 i 个字符与 p 中的前 j个字符是否能够匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        # dp[0][0] 相当于两个空串很自然就匹配上了
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # p不可能以'*'开头，所以j-1=='*'表明，j至少>=2时才会出现*
                    # 当p[j-1] == '*'时可以认为是否匹配决定于p[j-2]与s[i]是否匹配。
                    dp[i][j] |= dp[i][j - 2]
                    if matches(i, j - 1):
                        # 如果s[i-1]与p[j-2]匹配，那么p[j-2]对应的字符可以匹配s中1个或多个。
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if matches(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
        return dp[m][n]


# leetcode submit region end(Prohibit modification and deletion)
