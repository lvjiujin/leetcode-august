# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  测试用例的答案是一个 32-位 整数。 
# 
#  子数组 是数组的连续子序列。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10 <= nums[i] <= 10 
#  nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数 
#  
# 
#  Related Topics 数组 动态规划 👍 1854 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 考虑当前位置如果是一个负数的话，那么我们希望以它前一个位置结尾的某个段的积也是个负数，
    # 这样就可以负负得正，并且我们希望这个积尽可能「负得更多」，即尽可能小。
    # 如果当前位置是一个正数的话，我们更希望以它前一个位置结尾的某个段的积也是个正数，
    # 并且希望它尽可能地大


    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxF, minF, ans = nums[0], nums[0], nums[0]
        for i in range(1, n):
            ma, mi = maxF, minF
            maxF = max(ma * nums[i], mi * nums[i], nums[i])
            minF = min(mi * nums[i], ma * nums[i], nums[i])
            ans = max(ans, maxF)
        return ans

    def maxProduct2(self, nums: List[int]) -> int:
        n = len(nums)
        maxF = [0] * n
        minF = [0] * n
        maxF[0], minF[0] = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, n):
            maxF[i] = max(maxF[i - 1] * nums[i], minF[i - 1] * nums[i], nums[i])
            minF[i] = min(minF[i - 1] * nums[i], maxF[i - 1] * nums[i], nums[i])
            ans = max(maxF[i], ans)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
