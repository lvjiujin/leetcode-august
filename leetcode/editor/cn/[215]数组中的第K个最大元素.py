# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 
# 
#  请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列） 👍 1923 👎 0
import random


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        start, end = 0, len(nums) - 1
        target = len(nums) - k

        def partition(nums, start, end):
            # pivot = random.randint(0, end) 这个随机数很有问题，不能用。
            pivot = start + (end - start) // 2
            # print("pivot = {}, start = {}, end = {} ".format(pivot, start, end))
            # 交换pivot和end所指向的值。
            nums[pivot], nums[end] = nums[end], nums[pivot]
            small = start - 1
            for i in range(start,end):
                if nums[i] < nums[end]:
                    small += 1
                    nums[i], nums[small] = nums[small], nums[i]
            small += 1
            nums[small], nums[end] = nums[end], nums[small]
            return small

        index = partition(nums, start, end)
        while index != target:
            if index > target:
                end = index - 1
            else:
                start = index + 1
            index = partition(nums, start, end)

        return nums[index]


# leetcode submit region end(Prohibit modification and deletion)
