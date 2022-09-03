# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i 
# - j) <= k 。如果存在，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,1], k = 3
# 输出：true 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,0,1,1], k = 1
# 输出：true 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,2,3,1,2,3], k = 2
# 输出：false 
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  0 <= k <= 10⁵ 
#  
#  Related Topics 数组 哈希表 滑动窗口 👍 481 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 方法一：传统方法，采用两两比较的方法
        if not nums or len(nums) <2:
            return False
        d = dict()
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = [i]
            else:
                d[num].append(i)
        for value in d.values():
            n = len(value)
            if n > 1:
                for j in range(n-1):
                    if abs(value[j] - value[j+1]) <= k:
                        return True

        return False

        # 方法二：采用集合的方法。这个为什么呢？
        # if not nums:
        #     return False
        # s = set()
        # for i, num in enumerate(nums):
        #     if i > k:
        #         s.remove(nums[i-k-1])
        #     if num in s:
        #         return True
        #     s.add(num)
        # return False

        # 方法三，采用了词典的方法。
        # d = dict()
        # for i, num in enumerate(nums):
        #     if num in d and i - d[num] <= k:
        #         return True
        #     d[num] = i
        # return False
        # 当首次出现两个重复元素，而他们的索引差的绝对值不小于k，
        # 说明了一个问题那就是绝对值的差大于k，所以果断抛弃掉前一个值，用当前值代替前一个值。
        # seen = {}
        # for i in range(len(nums)):
        #     if nums[i] in seen and i - seen[nums[i]] <= k:
        #         return True
        #     seen[nums[i]] = i
        # return False

# leetcode submit region end(Prohibit modification and deletion)
