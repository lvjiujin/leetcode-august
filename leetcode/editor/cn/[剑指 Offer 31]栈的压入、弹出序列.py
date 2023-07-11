# 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈
# 的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# 输出：true
# 解释：我们可以按以下顺序执行：
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#  
# 
#  示例 2： 
# 
#  输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# 输出：false
# 解释：1 不能在 2 之前弹出。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= pushed.length == popped.length <= 1000 
#  0 <= pushed[i], popped[i] < 1000 
#  pushed 是 popped 的排列。 
#  
# 
#  注意：本题与主站 946 题相同：https://leetcode-cn.com/problems/validate-stack-sequences/ 
# 
#  Related Topics 栈 数组 模拟 👍 390 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed and not popped:
            return True
        if not pushed or not popped or len(pushed) != len(popped):
            return False
        stack = []
        curr = 0
        # 遍历数组 pushed，将 pushed 的每个元素依次入栈；
        # 每次将 pushed的元素入栈之后，如果栈不为空且栈顶元素与popped 的当前元素相同，
        # 则将栈顶元素出栈，同时遍历数组 popped直到栈为空或栈顶元素与 popped 的当前元素不同。
        # 遍历数组 pushed结束之后，每个元素都按照数组 pushed 的顺序入栈一次。
        # 如果栈为空，则每个元素都按照数组 popped 的顺序出栈，返回 true

        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[curr]:
                stack.pop()
                curr += 1

        return len(stack) == 0

# leetcode submit region end(Prohibit modification and deletion)
