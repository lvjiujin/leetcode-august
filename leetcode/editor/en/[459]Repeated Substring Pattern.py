# Given a string s, check if it can be constructed by taking a substring of it 
# and appending multiple copies of the substring together. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aba"
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" 
# twice.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of lowercase English letters. 
#  
#  Related Topics String String Matching 👍 3355 👎 319


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        """
        # algorithm 1
        n = len(s)
        for i in range(1, n//2 +1):
            if n %i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True
        return False

        # algorithm 2
        n = len(s)
        temp = []
        for i in range(1, n//2 + 1):
            if n % i == 0:
                temp.append(i)
        for j in temp:
            if s[:j] * (n // j) == s:
                return True
        return False

        # algorithm 3
        ss = s + s
        return s in ss[1:-1]

        # kmp algorithm 
        """




# leetcode submit region end(Prohibit modification and deletion)
