# 给定一个字符串 s ，请将 s 分割成一些子串，使每个子串都是 回文串 ，返回 s 所有可能的分割方案。 
# 
#  
#  回文串 是正着读和反着读都一样的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "google"
# 输出：[["g","o","o","g","l","e"],["g","oo","g","l","e"],["goog","l","e"]]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a"
# 输出：[["a"]] 
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
#  
# 
#  
#  注意：本题与主站 131 题相同： https://leetcode-cn.com/problems/palindrome-partitioning/ 
# 
#  Related Topics 深度优先搜索 广度优先搜索 图 哈希表 👍 42 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # 这个判断回文的方法非常独特，要好好理解一番。
        f = [[True] * n for _ in range(n)]
        # 因为外层循环实际上取不到n-1,因为内层循环i+1下标越界，所以实际上当i=n-1时内层循环没有执行
        # 所以这里可以优化成下标从i = n-2开始.
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret

    def partition2(self, s: str) -> List[List[str]]:
        # 分割回文串的回朔法
        result = []

        def backTrack(s, substrings, start, result):
            if start == len(s):
                result.append(substrings[:])
                return
            for i in range(start, len(s)):
                if isPalindrome(s, start, i):
                    substrings.append(s[start:i+1])
                    backTrack(s, substrings, i+1, result)
                    substrings.pop()

        def isPalindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        backTrack(s, [], 0, result)
        return result

# leetcode submit region end(Prohibit modification and deletion)
