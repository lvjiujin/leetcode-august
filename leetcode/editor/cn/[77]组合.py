# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。 
# 
#  你可以按 任何顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, k = 2
# 输出：
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
# 
#  示例 2： 
# 
#  
# 输入：n = 1, k = 1
# 输出：[[1]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
# 
#  Related Topics 回溯 👍 1169 👎 0



# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combination, result = [], []

        def helper(n, k, i, combination, result):
            if len(combination) == k:
                result.append(combination.copy())
            elif i <= n:
                helper(n, k, i + 1, combination, result)
                combination.append(i)
                helper(n, k, i + 1, combination, result)
                combination.pop()
        helper(n, k, 1, combination, result)

        return result

# leetcode submit region end(Prohibit modification and deletion)
