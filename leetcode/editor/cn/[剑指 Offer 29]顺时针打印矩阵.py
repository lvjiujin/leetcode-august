# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  限制： 
# 
#  
#  0 <= matrix.length <= 100 
#  0 <= matrix[i].length <= 100 
#  
# 
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/ 
# 
#  Related Topics 数组 矩阵 模拟 👍 468 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total
        # directions 这四个方向非常关键，不能乱了顺序：分别是向右，向下，向左，向上。
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow = row + directions[directionIndex][0]
            nextColumn = column + directions[directionIndex][1]
            # 只有当nextRow, nextColumn越界之后才转换到下一个方向（四个方向：向右，向下，向左，向上）
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and
                    not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4

            # 不断沿着同一个方向前进。
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]

        return order
# leetcode submit region end(Prohibit modification and deletion)
