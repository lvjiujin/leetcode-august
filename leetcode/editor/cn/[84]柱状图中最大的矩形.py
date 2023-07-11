# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入： heights = [2,4]
# 输出： 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= heights.length <=10⁵ 
#  0 <= heights[i] <= 10⁴ 
#  
# 
#  Related Topics 栈 数组 单调栈 👍 2130 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        maxArea = 0
        for i in range(len(heights)):
            while len(stack) > 0 and stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                width = i if len(stack) == 0 else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        while len(stack) > 0 and stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) if len(stack) == 0 else len(heights) - stack[-1] - 1
            maxArea = max(maxArea, height * width)
        return maxArea
        # 方法二 效率更高些
        # n = len(heights)
        # # left 和 right分别代表左右边界.
        # left, right = [0] * n, [n] * n
        #
        # mono_stack = list()
        # for i in range(n):
        #     # 栈顶高度大于等于当前高度时，实际上找到了计算矩形面积的一个右边界.
        #     while mono_stack and heights[mono_stack[-1]] >= heights[i]:
        #         # mono_stack[-1]
        #         right[mono_stack[-1]] = i # 右边界为i
        #         mono_stack.pop()
        #     # 栈顶高度小于当前高度时，实际上找到了计算矩形面积的一个左边界.
        #     left[i] = mono_stack[-1] if mono_stack else -1
        #     mono_stack.append(i)
        #
        # ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        # return ans



# leetcode submit region end(Prohibit modification and deletion)
