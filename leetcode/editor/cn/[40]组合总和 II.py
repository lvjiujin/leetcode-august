# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用 一次 。 
# 
#  注意：解集不能包含重复的组合。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ] 
# 
#  示例 2: 
# 
#  
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ] 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
# 
#  Related Topics 数组 回溯 👍 1138 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import copy
class Solution:
    # 回朔法
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target > sum(candidates):
            return []
        candidates.sort()
        result = []
        track = []
        # 这个回朔法真的很优美！值得学习。

        def backtrack(candidates, target, index):
            if sum(track) == target and track not in result:
                result.append(track.copy())
                return
            for i in range(index, len(candidates)):
                c = candidates[i]
                if c + sum(track) > target:
                    break
                if i > index and candidates[i] == candidates[i - 1]:  # TODO 对于可以重复的数组，一定要注意剪枝
                    continue
                track.append(c)
                backtrack(candidates, target, i + 1)
                track.pop()

        backtrack(candidates, target, 0)
        return result

    def combinationSum22(self, candidates: List[int], target: int) -> List[List[int]]:

        if target > sum(candidates):
            return []
        result = []
        combination = []
        candidates.sort()

        def getNext(nums, index):
            nxt = index
            while nxt < len(nums) and nums[nxt] == nums[index]:
                nxt += 1
            return nxt

        def helper(nums, target, i, combinaiton, result):
            if target == 0:
                result.append(copy.copy(combinaiton))
            elif target > 0 and i < len(nums):
                helper(nums, target, getNext(nums, i), combinaiton, result)
                combinaiton.append(nums[i])
                helper(nums, target - nums[i], i + 1, combinaiton, result)
                combinaiton.pop()
        helper(candidates, target, 0, combination, result)

        return result


# leetcode submit region end(Prohibit modification and deletion)
