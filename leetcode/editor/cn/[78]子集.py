# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  nums 中的所有元素 互不相同 
#  
# 
#  Related Topics 位运算 数组 回溯 👍 1824 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return None
        result = []

        def helper(nums, idx, subset, result):
            if idx == len(nums):
                result.append(subset.copy())
            elif idx < len(nums):
                helper(nums, idx + 1, subset, result)
                subset.append(nums[idx])
                helper(nums, idx + 1, subset, result)
                subset.pop()
        helper(nums, 0, [], result)
        return result


# leetcode submit region end(Prohibit modification and deletion)
