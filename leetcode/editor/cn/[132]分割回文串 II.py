# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。 
# 
#  返回符合要求的 最少分割次数 。 
# 
#  
#  
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "ab"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 2000 
#  s 仅由小写英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 👍 629 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        isPal = [[True] * n for _ in range(n)]
        # 由于 isPal[i][j] 依赖于状态 isPal[i+1][j−1]，
        # 因此需要我们左端点 i 是「从大到小」进行遍历；而右端点 j 是「从小到大」进行遍历。
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                isPal[i][j] = (s[i] == s[j]) and isPal[i+1][j-1]

        dp = [0 for _ in range(n)]

        for i in range(n):
            if isPal[0][i]:
                dp[i] = 0  # 0~i 是回文，不用分割，故次数为0
            else:
                dp[i] = i  # 先设定一个最大分割次数0~i共i+1个字符，最多i个分割次数
                for j in range(1, i+1):
                    if isPal[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)

        return dp[n - 1]
# leetcode submit region end(Prohibit modification and deletion)
