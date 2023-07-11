# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 1963 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numIslands2(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def dfs_marking(grid, i, j):
            nonlocal m, n
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return
            # 这两行对grid的赋值操作，是为了避免重复访问。
            grid[0][0] = '0'
            grid[i][j] = '0'
            dfs_marking(grid, i + 1, j)
            dfs_marking(grid, i - 1, j)
            dfs_marking(grid, i, j + 1)
            dfs_marking(grid, i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs_marking(grid, i, j)

        return count

    def numIslands1(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        # 每搜索一个子图，岛屿数量就加1.因为 存在visited的缘故，不会重复计算。
        def searchSubGraph(grid, visited, i, j):
            queue = [[i, j]]
            visited[i][j] = True
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while queue:
                pos = queue.pop()
                for dir in dirs:
                    r = dir[0] + pos[0]
                    c = dir[1] + pos[1]
                    if (0 <= r < len(grid) and
                            0 <= c < len(grid[0]) and
                            grid[r][c] == '1' and not visited[r][c]):
                        visited[r][c] = True
                        queue.append([r, c])

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    searchSubGraph(grid, visited, i, j)
                    count += 1

        return count
# leetcode submit region end(Prohibit modification and deletion)
