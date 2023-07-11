# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。 
# 
#  示例 1: 
# 
#  
# 输入：s = "abaccdeff"
# 输出：'b'
#  
# 
#  示例 2: 
# 
#  
# 输入：s = "" 
# 输出：' '
#  
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 50000 
# 
#  Related Topics 队列 哈希表 字符串 计数 👍 272 👎 0
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def firstUniqChar(self, s: str) -> str:
        # 哈希表
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = dic.get(c, 0) +1

        for key in dic:
            if dic[key] == 1:
                return key

        return " "

# leetcode submit region end(Prohibit modification and deletion)
