# 请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配
# 是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。 
# 
#  示例 1: 
# 
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3: 
# 
#  输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  示例 4: 
#
#  输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#  
# 
#  示例 5: 
# 
#  输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false 
# 
#  
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。 
#  
# 
#  注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/
#  
# 
#  Related Topics 递归 字符串 动态规划 👍 471 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

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

    def isMatch(self, s: str, p: str) -> bool:
        map = dict()

        def dp(i, j):
            m, n = len(s), len(p)
            if j == n:
                return i == m
            if i == m:
                # 此时还要判断p剩余部分是否是x*交替出现。
                # 剩余部分必定是偶数才能匹配。
                if (n - j) % 2 == 1:
                    return False
                while j + 1 < n:
                    if p[j+1] != "*":
                        return False
                    j += 2
                return True
            key = str(i) + "," + str(j)
            if key in map:
                return map[key]
            if s[i] == p[j] or p[j] == '.':
                if j + 1 < n and p[j+1] == '*':
                    # 当s[i] = p[j] 并且p[j+1] == '*'时，可以匹配零次，即j跳到j+2
                    # 也可以匹配1次或多次,用p[j]继续匹配s[i+1]等等。
                    res = dp(i, j+2) or dp(i+1, j)
                else:
                    res = dp(i+1, j+1)
            else:
                if j + 1 < n - 1 and p[j+1] == '*':
                    # 当p[j]不匹配s[i]时，如果p[j+1] == '*'就可以当成匹配零次，
                    # 所以有j+2，用p[j+2]重新匹配s[i]
                    res = dp(i, j+2)
                else:
                    res = False

            map[key] = res

            return res

        return dp(0, 0)






# leetcode submit region end(Prohibit modification and deletion)
