# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。 
# 
#  示例: 
# 
#  
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7 
# 
#  
# 
#  提示： 
# 
#  你可以假设 k 总是有效的，在输入数组 不为空 的情况下，1 ≤ k ≤ nums.length。 
# 
#  注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/ 
# 
#  Related Topics 队列 滑动窗口 单调队列 堆（优先队列） 👍 509 👎 0
import collections
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        # 单调递减队列:
        q = collections.deque()
        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                # 当相等的时候，肯定是要新值不要老值
                q.pop()
            q.append(i)
        ans = [nums[q[0]]]

        for i in range(k, n):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            while q[0] <= i-k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        ans = [-q[0][0]]

        for i in range(k, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i-k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans
# leetcode submit region end(Prohibit modification and deletion)
