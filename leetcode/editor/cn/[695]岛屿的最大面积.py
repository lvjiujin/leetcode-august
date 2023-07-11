# 给你一个大小为 m x n 的二进制矩阵 grid 。 
# 
#  岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都
# 被 0（代表水）包围着。 
# 
#  岛屿的面积是岛上值为 1 的单元格的数目。 
# 
#  计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,
# 0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,
# 0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 输出：6
# 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[0,0,0,0,0,0,0,0]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 50 
#  grid[i][j] 为 0 或 1 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 868 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def getArea(grid, visited, i, j):
            queue = [[i, j]]
            area = 0
            visited[i][j] = True
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while queue:
                pos = queue.pop()
                area += 1
                for dir in dirs:
                    r = dir[0] + pos[0]
                    c = dir[1] + pos[1]
                    if (0 <= r < len(grid) and
                            0 <= c < len(grid[0]) and
                        grid[r][c] == 1 and not visited[r][c]):
                        visited[r][c] = True
                        queue.append([r, c])
            return area

        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    area = getArea(grid, visited, i, j)
                    maxArea = max(maxArea, area)
        return maxArea
    # 思考一下，如何求岛屿个数？


# leetcode submit region end(Prohibit modification and deletion)
