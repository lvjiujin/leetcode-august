# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现
# 在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
#  
# 
#  示例 2: 
# 
#  
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
#  
# 
#  示例 3: 
# 
#  
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= temperatures.length <= 10⁵ 
#  30 <= temperatures[i] <= 100 
#  
# 
#  Related Topics 栈 数组 单调栈 👍 1328 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # 如果当前温度比栈顶温度高，栈顶温度将出栈.所以每次入栈的温度一定比栈顶温度低或相同。
                # 即栈中的温度是递减排序的。
                prev = stack.pop()
                # 如果当前温度比栈顶温度高，那么就知道位于栈顶的那一天需要等待几天才会出现更高的问题。
                # 然后出栈一次，再与下一个栈顶温度进行比较。
                result[prev] = i - prev
            stack.append(i)
        return result

# leetcode submit region end(Prohibit modification and deletion)
