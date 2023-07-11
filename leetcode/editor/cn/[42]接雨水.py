# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
#  
# 
#  示例 2： 
# 
#  
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= height[i] <= 10⁵ 
#  
# 
#  Related Topics 栈 数组 双指针 动态规划 单调栈 👍 3912 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                high = min(height[i], height[left]) - height[top]
                ans += width * high
            stack.append(i)
        return ans

    def trap2(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        i, j = 0, len(height) - 1
        left_max, right_max = 0, 0
        rain_water = 0
        while i <= j:
            left_max = max(height[i], left_max)
            right_max = max(height[j], right_max)
            if height[i] < height[j]:
                rain_water += left_max - height[i]
                i += 1
            else:
                rain_water += right_max - height[j]
                j -= 1
        return rain_water





# leetcode submit region end(Prohibit modification and deletion)
