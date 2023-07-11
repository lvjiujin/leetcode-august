# 给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：timePoints = ["23:59","00:00"]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：timePoints = ["00:00","23:59","00:00"]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= timePoints.length <= 2 * 10⁴ 
#  timePoints[i] 格式为 "HH:MM" 
#  
# 
#  Related Topics 数组 数学 字符串 排序 👍 220 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        minuteFlags = [False for _ in range(1440)]
        for time in timePoints:
            ss = time.split(":")
            minutes = int(ss[0]) * 60 + int(ss[1]);
            if minuteFlags[minutes]:
                return 0
            minuteFlags[minutes] = True

        def helper(minFlags):
            minDiff = len(minFlags) - 1
            first = len(minFlags) - 1
            last = -1
            prev = -1
            for i in range(len(minFlags)):
                if minFlags[i]:
                    if prev >= 0:
                        minDiff = min(minDiff, i - prev)
                    prev = i
                    first = min(first, i)
                    last = max(last, i)
            return min(minDiff, first + len(minFlags) - last)

        return helper(minuteFlags)

# leetcode submit region end(Prohibit modification and deletion)
