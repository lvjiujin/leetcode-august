# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。 
# 
#  两个相邻元素间的距离为 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：[[0,0,0],[0,1,0],[0,0,0]]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
# 输出：[[0,0,0],[0,1,0],[1,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 10⁴ 
#  1 <= m * n <= 10⁴ 
#  mat[i][j] is either 0 or 1. 
#  mat 中至少有一个 0 
#  
# 
#  Related Topics 广度优先搜索 数组 动态规划 矩阵 👍 772 👎 0

import collections
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dists = [[0] * n for _ in range(m)]
        import collections
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dists[i][j] = 0
                    queue.append([i, j])
                else:
                    dists[i][j] = m + n

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:
            pos = queue.popleft()
            dist = dists[pos[0]][pos[1]]
            for dir in dirs:
                r = dir[0] + pos[0]
                c = dir[1] + pos[1]
                if 0 <= r < m and 0 <= c < n and dists[r][c] > dist + 1:
                    dists[r][c] = dist + 1
                    queue.append([r, c])
        return dists

    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dists = [[0] * n for _ in range(m)]
        # 将所有的 0 添加进初始队列中
        zeroes_pos = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        queue = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        # 广度优先搜索
        while queue:
            i, j = queue.popleft()
            for r, c in {(i-1, j), (i+1, j), (i, j-1), (i, j+1)}:
                if 0 <= r < m and 0 <= c < n and (r, c) not in seen:
                    dists[r][c] = dists[i][j] + 1
                    queue.append((r, c))
                    seen.add((r, c))
        return dists


# leetcode submit region end(Prohibit modification and deletion)
