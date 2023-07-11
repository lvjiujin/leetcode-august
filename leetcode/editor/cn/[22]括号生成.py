# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：["()"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 8 
#  
# 
#  Related Topics 字符串 动态规划 回溯 👍 2914 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(left, right, parenthesis, result):
            if left == 0 and right == 0:
                result.append(parenthesis)
            if left > 0:
                helper(left - 1, right, parenthesis + "(", result)
            if left < right:
                helper(left, right - 1, parenthesis + ")", result)
        helper(n, n , "", result)
        return result

# leetcode submit region end(Prohibit modification and deletion)
