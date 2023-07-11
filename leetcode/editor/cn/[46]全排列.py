# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  nums 中的所有整数 互不相同 
#  
# 
#  Related Topics 数组 回溯 👍 2262 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute3(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []

        # 主要思想回朔法:backtrack
        def dfs(nums, path, size, used, res):
            if len(path) == size:
                # 这个地方是个大坑。变量 path 所指向的列表 在深度优先遍历的过程中只有一份 ，深度优先遍历完成以后，回到了根结点，成为空列表。
                # path[:] 是path的一个拷贝：
                res.append(path[:])
                return
            # 在非叶子结点处，产生不同的分支，这一操作的语义是：在还未选择的数中依次选择一个元素作为下一个位置的元素，这显然得通过一个循环实现。
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    # print(" recursion before => " ,path)
                    dfs(nums, path, size, used, res)
                    # print(" recursion after => " , path)
                    # 注意：下面这两行代码发生 「回溯」，回溯发生在从 深层结点 回到 浅层结点 的过程，代码在形式上和递归之前是对称的
                    used[i] = False
                    path.pop()
                    # print("path = ", path)

        res, path, size = [], [], len(nums)
        used = [False for _ in range(size)]
        dfs(nums, path, size, used, res)

        return res

    def permute(self, nums: List[int]) -> List[List[int]]:

        def backTrack(nums, i, result):
            if i == len(nums):
                permutation = []
                for num in nums:
                    permutation.append(num)
                result.append(permutation)
            else:
                for j in range(i, len(nums)):
                    nums[i], nums[j] = nums[j], nums[i]
                    backTrack(nums, i+1, result)
                    nums[i], nums[j] = nums[j], nums[i]

        result = []
        backTrack(nums, 0, result)
        return result

# leetcode submit region end(Prohibit modification and deletion)
