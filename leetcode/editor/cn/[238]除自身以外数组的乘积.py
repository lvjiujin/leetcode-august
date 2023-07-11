# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。 
# 
#  题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内。 
# 
#  请不要使用除法，且在 O(n) 时间复杂度内完成此题。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁵ 
#  -30 <= nums[i] <= 30 
#  保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位 整数范围内 
#  
# 
#  
# 
#  进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。） 
# 
#  Related Topics 数组 前缀和 👍 1315 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # space comlexity O(1)
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = dp[i - 1] * nums[i - 1]
        right = 1
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i] * right
            right *= nums[i]
        return dp

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        # space complexity O(n)
        n = len(nums)
        left, right = [0] * n, [0] * n
        left[0] = 1
        right[n - 1] = 1
        dp = [0] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            dp[i] = left[i] * right[i]

        return dp
# leetcode submit region end(Prohibit modification and deletion)
