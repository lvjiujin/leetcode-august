# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
# 
#  Related Topics 数组 回溯 👍 1220 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backTrack(nums, i, result):
            if i == len(nums):
                permutation = []
                for num in nums:
                    permutation.append(num)
                result.append(permutation)
            else:
                set1 = set()
                for j in range(i, len(nums)):
                    if nums[j] not in set1:
                        set1.add(nums[j])
                        nums[i], nums[j] = nums[j], nums[i]
                        backTrack(nums, i + 1, result)
                        nums[i], nums[j] = nums[j], nums[i]

        result = []
        backTrack(nums, 0, result)
        return result


# leetcode submit region end(Prohibit modification and deletion)
