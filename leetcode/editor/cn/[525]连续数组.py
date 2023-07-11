# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。 
# 
#  示例 2: 
# 
#  
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums[i] 不是 0 就是 1 
#  
# 
#  Related Topics 数组 哈希表 前缀和 👍 587 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # max_len = 0
        # map = dict()
        # map[0] = -1
        # result = 0
        # for i in range(len(nums)):
        #     result += -1 if nums[i] == 0 else 1
        #     if result in map.keys():
        #         max_len = max(max_len, i - map[result])
        #     else:
        #         map[result] = i
        #
        # return max_len
        # 方法二：
        # 前缀和字典: key为1的数量和0的数量的差值,value为对应坐标
        # hashmap = {0: -1}
        # # 当前1的数量和0的数量的差值
        # counter = ans = 0
        # for i, num in enumerate(nums):
        #     # 每多一个1，差值+1
        #     if num:
        #         counter += 1
        #     # 每多一个0，差值-1
        #     else:
        #         counter -= 1
        #     # 如果存在1和0的数量差值相等的地方，那么说明后者到前者之前1和0的数量相等！
        #     if counter in hashmap:
        #         ans = max(ans, i - hashmap[counter])
        #     else:
        #         hashmap[counter] = i
        # return ans
        # 方法三 效率最高
        pre = {0: -1}
        ans = cur = 0
        for i, num in enumerate(nums):
            cur += (2 * num - 1)
            if cur in pre and i - pre[cur] > ans:
                ans = i - pre[cur]
            if cur not in pre:
                pre[cur] = i
        return ans



# leetcode submit region end(Prohibit modification and deletion)
