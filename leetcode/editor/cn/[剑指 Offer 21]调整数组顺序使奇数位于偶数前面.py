# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4] 
# 注：[3,1,2,4] 也是正确的答案之一。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 50000 
#  0 <= nums[i] <= 10000 
#  
# 
#  Related Topics 数组 双指针 排序 👍 267 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:

        res1 = []
        res2 = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                res2.append(nums[i])
            else:
                res1.append(nums[i])
        res1.extend(res2)
        return res1
# leetcode submit region end(Prohibit modification and deletion)
