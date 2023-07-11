# 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。 
# 
#  对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
# 输出：4 
# 解释：最长递增路径为 [1, 2, 6, 9]。 
# 
#  示例 2： 
#  
#  
# 输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
# 输出：4 
# 解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [[1]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 200 
#  0 <= matrix[i][j] <= 2³¹ - 1 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 记忆化搜索 数组 动态规划 矩阵 👍 718 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        lengths = [[0] * n for _ in range(m)]

        def dfs(matrix, lengths, i, j):
            if lengths[i][j] > 0:
                return lengths[i][j]
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            length = 1
            for dir in dirs:
                r = dir[0] + i
                c = dir[1] + j
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > matrix[i][j]:
                    path = dfs(matrix, lengths, r, c)
                    length = max(path + 1, length)
            lengths[i][j] = length
            return length

        longest = 0
        for i in range(m):
            for j in range(n):
                length = dfs(matrix, lengths, i, j)
                longest = max(longest, length)
        return longest

# leetcode submit region end(Prohibit modification and deletion)
