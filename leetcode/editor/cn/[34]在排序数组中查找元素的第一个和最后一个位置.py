# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums 是一个非递减数组 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics 数组 二分查找 👍 2000 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and target == nums[0]:
            return [0, 0]
        # 二分查找:
        left, right = 0, len(nums) - 1
        pos = -1
        while left <= right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                # 找到了其中的一个元素, 就可以退出该循环了
                pos = mid
                break
        if pos == -1:
            return [-1, -1]
        mid_left = pos - 1
        while mid_left >= 0 and nums[mid_left] == target:
            mid_left -= 1
        mid_left += 1

        mid_right = pos + 1

        while mid_right < len(nums) and nums[mid_right] == target:
            mid_right += 1

        mid_right -= 1

        return [mid_left, mid_right]


# leetcode submit region end(Prohibit modification and deletion)
