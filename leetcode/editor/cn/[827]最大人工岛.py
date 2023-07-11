# 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。 
# 
#  返回执行此操作后，grid 中最大的岛屿面积是多少？ 
# 
#  岛屿 由一组上、下、左、右四个方向相连的 1 形成。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: grid = [[1, 0], [0, 1]]
# 输出: 3
# 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
#  
# 
#  示例 2: 
# 
#  
# 输入: grid = [[1, 1], [1, 0]]
# 输出: 4
# 解释: 将一格0变成1，岛屿的面积扩大为 4。 
# 
#  示例 3: 
# 
#  
# 输入: grid = [[1, 1], [1, 1]]
# 输出: 4
# 解释: 没有0可以让我们变成1，面积依然为 4。 
# 
#  
# 
#  提示： 
# 
#  
#  n == grid.length 
#  n == grid[i].length 
#  1 <= n <= 500 
#  grid[i][j] 为 0 或 1 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 298 👎 0
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        n = len(grid)
        tags = [[0] * n for _ in range(n)]
        areas = collections.Counter()

        def dfs(i, j):

            tags[i][j] = t
            areas[t] += 1
            for xi, yi in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= xi < n and 0 <= yi < n and grid[xi][yi] and tags[xi][yi] == 0:
                    dfs(xi, yi)

        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value and tags[i][j] == 0: # 枚举还没有访问过的陆地
                    t = i * n + j + 1
                    dfs(i, j)

        ans = max(areas.values(), default=0)
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == 0: # 枚举可以添加陆地的位置
                    newArea = 1
                    connected = {0} #
                    # 对于每个 grid[i][j]=0，我们计算将它变为 1 后，新合并的岛屿的面积 z（z 的初始值为 1，对应该点的面积）
                    # 使用集合 connected 保存与 grid[i][j]相连的岛屿
                    # 遍历与 grid[i][j]相邻的四个点，如果该点的值为 1，且它所在的岛屿并不在集合中，
                    # 我们将 z 加上该点所在的岛屿面积，并且将该岛屿加入集合中。
                    # 所有这些新合并岛屿以及原来的岛屿的面积的最大值就是最大的岛屿面积。
                    for xi, yi in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= xi < n and 0 <= yi < n and tags[xi][yi] not in connected:
                            connected.add(tags[xi][yi])
                            newArea += areas[tags[xi][yi]]
                    print("newArea = ", newArea)
                    ans = max(ans, newArea)

        return ans


# leetcode submit region end(Prohibit modification and deletion)
