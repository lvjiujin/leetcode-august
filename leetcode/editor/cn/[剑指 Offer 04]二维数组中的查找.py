# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个
# 整数，判断数组中是否含有该整数。 
# 
#  
# 
#  示例: 
# 
#  现有矩阵 matrix 如下： 
# 
#  
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#  
# 
#  给定 target = 5，返回 true。 
# 
#  给定 target = 20，返回 false。 
# 
#  
# 
#  限制： 
# 
#  0 <= n <= 1000 
# 
#  0 <= m <= 1000 
# 
#  
# 
#  注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/ 
# 
#  Related Topics 数组 二分查找 分治 矩阵 👍 813 👎 0
import bisect


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 二分查找
        for row in matrix:
            idx = bisect.bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True
        return False

    def findNumberIn2DArray2(self, matrix: List[List[int]], target: int) -> bool:
        # Z字形查找， 每次排除掉一行或一列，时间复杂度O(n)
        if not matrix:
            return False
        rows, columns = len(matrix), len(matrix[0])
        found = False

        if rows > 0 and columns > 0:
            row = 0
            column = columns - 1
            while row < rows and column>=0:
                result = matrix[row][column]
                if result == target:
                    found = True
                    return found
                elif result > target:
                    column -= 1
                else:
                    row += 1

        return found
# leetcode submit region end(Prohibit modification and deletion)
