# Given a string s, reverse the order of characters in each word within a 
# sentence while still preserving whitespace and initial word order. 
# 
#  
#  Example 1: 
#  Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#  Example 2: 
#  Input: s = "God Ding"
# Output: "doG gniD"
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  s contains printable ASCII characters. 
#  s does not contain any leading or trailing spaces. 
#  There is at least one word in s. 
#  All the words in s are separated by a single space. 
#  
#  Related Topics Two Pointers String 👍 2786 👎 167


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split(" ")
        res = []
        for x in s_split:
            x = x[::-1]
            res.append(x)
        return " ".join(res)

        
# leetcode submit region end(Prohibit modification and deletion)
