# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= 
# t ，同时又满足 abs(i - j) <= k 。 
# 
#  如果存在则返回 true，不存在返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false 
# 
#  
# 
#  提示：
# 
#  
#  0 <= nums.length <= 2 * 10⁴ 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  0 <= k <= 10⁴ 
#  0 <= t <= 2³¹ - 1 
#  
# 
#  Related Topics 数组 桶排序 有序集合 排序 滑动窗口 👍 657 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # 用桶方法来实现：这个效率并不高。
        buckets = dict()
        bucketSize = valueDiff + 1

        def getBucketId(num, bucketSize):
            return num // bucketSize if num >= 0 else (num + 1) // bucketSize -1
        for i in range(len(nums)):
            num = nums[i]
            idx = getBucketId(num, bucketSize)
            if (idx in buckets or ((idx - 1) in buckets and buckets[idx -1] + valueDiff >= num) or
                ((idx + 1) in buckets and buckets[idx + 1] - valueDiff <= num)):
                return True
            buckets[idx] = num
            if i >= indexDiff:
                buckets.pop(getBucketId(nums[i - indexDiff], bucketSize))
        return False
# leetcode submit region end(Prohibit modification and deletion)
