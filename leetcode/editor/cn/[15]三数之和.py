# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != 
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请 
# 
#  你返回所有和为 0 且不重复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics 数组 双指针 排序 👍 5170 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3 :
            return None
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n-2):

            if nums[i] > 0:
                # nums[i]第一个元素，如果比0大，那么后面没有必要再看了，直接返回结束。
                return result
            if i > 0 and nums[i] == nums[i-1]:
                # 确定第一个元素时，如果发现它与前面的值一样，跳过本轮循环。
                continue
            left = i + 1  # 第二个元素下标
            right = n - 1  # 第三个元素下标
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    temp = nums[left]
                    while left < right and nums[left] == temp:
                        left += 1
                    temp = nums[right]
                    while left < right and temp == nums[right]:
                        right -= 1

                elif s > 0:
                    right -= 1

                else:
                    left += 1

        return result



# leetcode submit region end(Prohibit modification and deletion)
