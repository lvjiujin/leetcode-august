# 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。 
# 
#  你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。 
# 
#  请你计算并返回达到楼梯顶部的最低花费。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：cost = [10,15,20]
# 输出：15
# 解释：你将从下标为 1 的台阶开始。
# - 支付 15 ，向上爬两个台阶，到达楼梯顶部。
# 总花费为 15 。
#  
# 
#  示例 2： 
# 
#  
# 输入：cost = [1,100,1,1,1,100,1,1,100,1]
# 输出：6
# 解释：你将从下标为 0 的台阶开始。
# - 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
# - 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
# - 支付 1 ，向上爬一个台阶，到达楼梯顶部。
# 总花费为 6 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= cost.length <= 1000 
#  0 <= cost[i] <= 999 
#  
# 
#  Related Topics 数组 动态规划 👍 1029 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 方法一：时间复杂度太高，不能通过的原始解法。
    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        length = len(cost)

        def helper(cost, i):
            if i < 2:
                return cost[i]
            return min(helper(cost, i - 2), helper(cost, i - 1)) + cost[i]

        return min(helper(cost, length -2), helper(cost, length - 1))

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0 for _ in range(length)]

        def helper(cost, i, dp):
            if i < 2:
                dp[0] = cost[0]
                dp[1] = cost[1]

            elif dp[i] == 0:

                helper(cost, i - 2, dp)
                helper(cost, i - 1, dp)
                dp[i] = min(dp[i-2], dp[i-1]) + cost[i]

        helper(cost, length - 1, dp)
        return min(dp[length - 2], dp[length - 1])

    def minCostClimbingStairs3(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0 for _ in range(length)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, length):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[length -1], dp[length -2])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0 for _ in range(2)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, length):
            dp[i % 2] = min(dp[0], dp[1]) + cost[i]
        return min(dp[0], dp[1])


# leetcode submit region end(Prohibit modification and deletion)
