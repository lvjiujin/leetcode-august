# Given two strings s and t, return true if t is an anagram of s, and false 
# otherwise. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: s = "anagram", t = "nagaram"
# Output: true
#  
#  Example 2: 
#  Input: s = "rat", t = "car"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s and t consist of lowercase English letters. 
#  
# 
#  
#  Follow up: What if the inputs contain Unicode characters? How would you 
# adapt your solution to such a case? 
# 
#  Related Topics Hash Table String Sorting 👍 6777 👎 238


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 方法一：没有技巧的笨办法
        # if not s or not t or len(s) != len(t):
        #     return False
        # d = dict()
        # for x in s:
        #     if x in d:
        #         d[x] +=1
        #     else:
        #         d[x] = 1
        # for y in t:
        #     if y not in d:
        #         return False
        #     else:
        #         d[y] -=1
        # for i in d.values():
        #     if i != 0:
        #         return False
        #
        # return True
    # 方法二: 一定要想到排序。一定要想到排序。
    #     if not s or not t or len(s) != len(t):
    #         return False
    #     s = sorted(s)
    #     t = sorted(t)
    #     if s == t:
    #         return True
    #     else:
    #         return False
    # 方法三：Counter
        from collections import Counter
        return Counter(s) == Counter(t)





        
# leetcode submit region end(Prohibit modification and deletion)
