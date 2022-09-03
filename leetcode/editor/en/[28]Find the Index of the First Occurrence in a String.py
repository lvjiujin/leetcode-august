# Given two strings needle and haystack, return the index of the first 
# occurrence of needle in haystack, or -1 if needle is not part of haystack. 
# 
#  
#  Example 1: 
# 
#  
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#  
# 
#  Example 2: 
# 
#  
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= haystack.length, needle.length <= 10⁴ 
#  haystack and needle consist of only lowercase English characters. 
#  
# 
#  Related Topics Two Pointers String String Matching 👍 0 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle not in haystack:
        #     return -1
        # else:
        #     has_lst = haystack.split(needle)[0]
        #     if len(has_lst) == 0:
        #         return 0
        #     else:
        #         return len(has_lst)
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)

        
# leetcode submit region end(Prohibit modification and deletion)
