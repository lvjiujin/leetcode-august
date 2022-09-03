# 给定一个字符串
#  s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
#  
# 
#  示例 2: 
# 
#  
# 输入： s = "God Ding"
# 输出："doG gniD"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  
#  s 包含可打印的 ASCII 字符。 
#  
#  s 不包含任何开头或结尾空格。 
#  
#  s 里 至少 有一个词。 
#  
#  s 中的所有单词都用一个空格隔开。 
#  
# 
#  Related Topics 双指针 字符串 👍 475 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseWords(self, s: str) -> str:
        # 思考一下，下列三种方法为什么能？方法一：一般方法比较容易理解。
        #
        # 方法一：先分割单词，然后将单词反转，最后再拼接
        # return " ".join([word[::-1] for word in s.split(" ")])
        # 方法二：先分割单词，再反转单词列表，组成字符串，最后反转字符串。
        # return " ".join([word for word in s.split(" ")][::-1])[::-1]
        # 方法三：先反转字符串，再反转单词列表,这种方法最好，没有用到列表循环。
        return " ".join(s[::-1].split(" ")[::-1])



# leetcode submit region end(Prohibit modification and deletion)
