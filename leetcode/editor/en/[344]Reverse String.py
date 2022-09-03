# Write a function that reverses a string. The input string is given as an 
# array of characters s. 
# 
#  You must do this by modifying the input array in-place with O(1) extra 
# memory. 
# 
#  
#  Example 1: 
#  Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#  Example 2: 
#  Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is a printable ascii character. 
#  
#  Related Topics Two Pointers String Recursion 👍 5044 👎 946


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(l//2):
            s[i], s[l-i-1] = s[l-i-1], s[i]

        # 双指针法:
        i, j = 0, len(s) -1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1

# leetcode submit region end(Prohibit modification and deletion)
