# 统计一个数字在排序数组中出现的次数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2 
# 
#  示例 2: 
# 
#  
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0 
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
#  
# 
#  注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-
# position-of-element-in-sorted-array/ 
# 
#  Related Topics 数组 二分查找 👍 373 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or (len(nums) == 1 and nums[0] != target):
            return 0

        left, right = 0, len(nums) - 1
        pos = -1
        while left <= right:
            mid = left + (right - left) //2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] <target:
                left = mid + 1
            else:
                pos = mid
                break

        if pos == -1:
            return 0
        left = pos -1
        while left >= 0 and nums[left] == target:
            left -= 1
        left += 1

        right = pos + 1
        while right < len(nums) and nums[right] == target:
            right += 1
        right -= 1
        return right - left + 1

# leetcode submit region end(Prohibit modification and deletion)
