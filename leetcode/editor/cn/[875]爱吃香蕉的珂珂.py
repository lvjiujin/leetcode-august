# 珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。 
# 
#  珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后
# 这一小时内不会再吃更多的香蕉。 
# 
#  珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。 
# 
#  返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：piles = [3,6,7,11], h = 8
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：piles = [30,11,23,4,20], h = 5
# 输出：30
#  
# 
#  示例 3： 
# 
#  
# 输入：piles = [30,11,23,4,20], h = 6
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= piles.length <= 10⁴ 
#  piles.length <= h <= 10⁹ 
#  1 <= piles[i] <= 10⁹ 
#  
# 
#  Related Topics 数组 二分查找 👍 441 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        return bisect_left(range(max(piles)), -h, 1, key=lambda k: -sum((pile + k - 1) // k for pile in piles))

    def minEatingSpeed2(self, piles: List[int], h: int) -> int:
        # bisect_left(range(max(piles)), -h, 1, key=lambda k: -sum((pile + k - 1) // k for pile in piles))

        # 为何这二分查找这么慢？
        longest = max(piles)
        left = 1
        right = longest

        def getHours(speed, bananas):
            hours = 0
            for banana in bananas:
                hours += ((banana + speed - 1) // speed)
            return hours

        while left <= right:
            mid = left + (right - left) //2
            hours = getHours(mid, piles)
            if hours <= h:
                if mid == 1 or getHours(mid - 1, piles)> h:
                    return mid
                right = mid - 1
            else:
                left = mid + 1


# leetcode submit region end(Prohibit modification and deletion)
