# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。 
# 
#  回文串 是正着读和反着读都一样的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：[["a"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 16 
#  s 仅由小写英文字母组成 
#  
# 
#  Related Topics 字符串 动态规划 回溯 👍 1297 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 回朔法
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)
        isPal = [[True] * n for _ in range(n)]

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                isPal[i][j] = (s[i] == s[j] and isPal[i+1][j-1])

        def backTrack(s, start, substrings, res):
            if start == len(s):

                res.append(substrings[:])
                return
            for i in range(start, len(s)):
                if isPal[start][i]:
                    substrings.append(s[start: i + 1])
                    backTrack(s, i + 1, substrings, res)
                    substrings.pop()
        # 不要采用这种方法进行判断，这种属于暴力方法，o(n^3)的时间复杂度。
        # def isPalindrome(ss, start, end):
        #     while start < end:
        #         if ss[start] != ss[end]:
        #             return False
        #         start += 1
        #         end -= 1
        #     return True

        backTrack(s, 0, [], result)
        return result
# leetcode submit region end(Prohibit modification and deletion)
