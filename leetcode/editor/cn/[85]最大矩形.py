# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = []
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：matrix = [["1"]]
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：matrix = [["0","0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == matrix.length 
#  cols == matrix[0].length 
#  1 <= row, cols <= 200 
#  matrix[i][j] 为 '0' 或 '1' 
#  
# 
#  Related Topics 栈 数组 动态规划 矩阵 单调栈 👍 1401 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        maxArea = 0
        heights = [0 for _ in range(len(matrix[0]))]

        def largestRectangleArea(heights: List[int]) -> int:
            n = len(heights)
            # left 和 right分别代表左右边界.
            left, right = [0] * n, [n] * n

            mono_stack = list()
            for j in range(n):
                # 栈顶高度大于等于当前高度时，实际上找到了计算矩形面积的一个右边界.
                while mono_stack and heights[mono_stack[-1]] >= heights[j]:
                    # mono_stack[-1]
                    right[mono_stack[-1]] = j  # 右边界为i
                    mono_stack.pop()
                # 栈顶高度小于当前高度时，实际上找到了计算矩形面积的一个左边界.
                left[j] = mono_stack[-1] if mono_stack else -1
                mono_stack.append(j)

            ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
            return ans

        for mat in matrix:
            for i in range(len(mat)):
                if mat[i] == '0':
                    heights[i] = 0
                else:
                    heights[i] += 1
            maxArea = max(maxArea, largestRectangleArea(heights))
        return maxArea;


# leetcode submit region end(Prohibit modification and deletion)
