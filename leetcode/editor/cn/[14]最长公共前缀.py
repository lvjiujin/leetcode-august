# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
#  
# 
#  示例 2： 
# 
#  
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] 仅由小写英文字母组成 
#  
# 
#  Related Topics 字符串 👍 2431 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        # prefix = strs[0]
        # n = len(strs)
        # for i in range(1, n):
        #     prefix = self.lcp(prefix, strs[i])
        #     if prefix == "":
        #         break
        # return prefix
        # 方法二：分治法的思想：
        # length, count = len(strs[0]), len(strs)
        # for i in range(length):
        #     c = strs[0][i]
        #     # 两种情况满足其一即可返回：某一个字符串结束了，或者某个字符串上某一列不匹配。
        #     if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
        #         return strs[0][:i]
        # # 如果前面没有返回，说明第一个字符串比较完了，第一个字符串就是最长公共前缀
        # return strs[0]
        # 分治法
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) - 1)



    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]



# leetcode submit region end(Prohibit modification and deletion)
