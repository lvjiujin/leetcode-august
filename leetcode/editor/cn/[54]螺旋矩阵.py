# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
# 
#  Related Topics 数组 矩阵 模拟 👍 1259 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows, columns = len(matrix), len(matrix[0])
        total = rows * columns
        visited = [[False] * columns for _ in range(rows)]
        order = [0] * total
        directions = [[0, 1],  # 向右
                      [1, 0],  # 向下
                      [0, -1], # 向左
                      [-1, 0]] # 向上
        newRow, newColumn, directionIndex = 0, 0, 0
        row, column = 0, 0

        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            newRow = row + directions[directionIndex][0]
            newColumn = column + directions[directionIndex][1]
            if not (0 <= newRow < rows and 0 <= newColumn < columns
                    and not visited[newRow][newColumn]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]

        return order




# leetcode submit region end(Prohibit modification and deletion)
