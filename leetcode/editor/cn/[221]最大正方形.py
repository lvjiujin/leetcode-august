# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：4
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 300 
#  matrix[i][j] 为 '0' 或 '1' 
#  
# 
#  Related Topics 数组 动态规划 矩阵 👍 1304 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        maxSide = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                    maxSide = max(maxSide, dp[i][j])

        return maxSide * maxSide
# leetcode submit region end(Prohibit modification and deletion)
