# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。 
# 
#  你必须设计并实现线性时间复杂度的算法且不使用额外空间来解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,2,3,2]
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 
#  
# 
#  Related Topics 位运算 数组 👍 927 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # 方法一，这种方法不适用于python，适用于java
        # result = 0
        # for i in range(32):
        #     total = 0
        #     for num in nums:
        #         total += ((num >> i) & 1)
        #     if total % 3 != 0:
        #
        #         result |= (1 << i)
        # return result
        # 这个位运算需要好好研究研究。
        X, Y = 0, 0
        for Z in nums:
            Y = Y ^ Z & ~X
            X = X ^ Z & ~Y
        return Y


# leetcode submit region end(Prohibit modification and deletion)
