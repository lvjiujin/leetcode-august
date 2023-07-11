# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的连续子数组的个数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1], k = 2
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3], k = 3
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -1000 <= nums[i] <= 1000 
#  -10⁷ <= k <= 10⁷ 
#  
# 
#  Related Topics 数组 哈希表 前缀和 👍 1691 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        map = dict()
        map[0] = 1  # 思考一下，这句代码为何很关键？
        count, result = 0, 0
        for num in nums:
            result += num
            count += map.get(result - k, 0)
            if result in map:
                map[result] += 1
            else:
                map[result] = 1

        return count
# leetcode submit region end(Prohibit modification and deletion)
