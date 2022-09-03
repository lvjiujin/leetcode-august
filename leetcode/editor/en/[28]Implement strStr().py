# Implement strStr(). 
# 
#  Given two strings needle and haystack, return the index of the first 
# occurrence of needle in haystack, or -1 if needle is not part of haystack. 
# 
#  Clarification: 
# 
#  What should we return when needle is an empty string? This is a great 
# question to ask during an interview. 
# 
#  For the purpose of this problem, we will return 0 when needle is an empty 
# string. This is consistent to C's strstr() and Java's indexOf(). 
# 
#  
#  Example 1: 
# 
#  
# Input: haystack = "hello", needle = "ll"
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= haystack.length, needle.length <= 10⁴ 
#  haystack and needle consist of only lowercase English characters. 
#  
#  Related Topics Two Pointers String String Matching 👍 4051 👎 3667


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 直接用kmp 算法来搞。
        if not haystack or not needle:
            return 0
        n, m = len(haystack), len(needle)
        def generate_next(p):
            m = len(p)
            next = [0 for _ in range(m)]
            left, right = 0, 1
            for right in range(1, m):
                if left > 0 and p[left]!= p[right]:
                    left = next[left - 1]
                if p[left] == p[right]:
                    left+=1
                next[right] = left
            return next
        next = generate_next(needle)
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j-1]
            if haystack[i] == needle[j]:
                j+=1
            if j == m:
                return i-j+1
        return -1

        
# leetcode submit region end(Prohibit modification and deletion)
