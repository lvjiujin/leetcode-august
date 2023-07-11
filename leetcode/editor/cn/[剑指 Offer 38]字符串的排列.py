# 输入一个字符串，打印出该字符串中字符的所有排列。 
# 
#  
# 
#  你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。 
# 
#  
# 
#  示例: 
# 
#  输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#  
# 
#  
# 
#  限制： 
# 
#  1 <= s 的长度 <= 8 
# 
#  Related Topics 字符串 回溯 👍 617 👎 0
import itertools


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def permutation4(self, s: str) -> List[str]:
        n = len(s)
        s_lst = list(s)
        visited = [False] * n
        res = set()

        def dfs(ss):
            if len(ss) == n:
                res.add(ss)
                return
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                dfs(ss + s_lst[i])
                visited[i] = False

        dfs("")
        return list(res)

    def permutation3(self, s: str) -> List[str]:
        s_lst, res = list(s), []
        # s有n个字符，可以看成是n个空位，即从左往右每一位空位都尝试填入一个字符，

        def backtrack(idx):
            if idx == len(s_lst) - 1:
                res.append(''.join(s_lst))  # 添加排列方案
                return
            dic = set()
            for i in range(idx, len(s_lst)):
                if s_lst[i] in dic:
                    continue  # 重复，因此剪枝
                dic.add(s_lst[i])
                s_lst[i], s_lst[idx] = s_lst[idx], s_lst[i]  # 交换，将 s_lst[i] 固定在第 idx 位
                backtrack(idx + 1)  # 开启固定第 idx + 1 位字符
                s_lst[i], s_lst[idx] = s_lst[idx], s_lst[i]  # 恢复交换

        backtrack(0)
        return res

    def permutation(self, s: str) -> List[str]:

        def nextPermutation(lst) -> bool:
            """
            Do not return anything, modify nums in-place instead.
            从后往前寻找非降序的a[i], 寻找a[j]，满足:a[i] < a[j],
            交换a[i]和a[j]，反转a[i+1:]之后的元素
            """

            i = len(lst) - 2
            while i >= 0 and lst[i] >= lst[i + 1]:
                i -= 1
            if i < 0:
                return False
            if i >= 0:
                j = len(lst) - 1
                while j >= 0 and lst[i] >= lst[j]:
                    j -= 1

                lst[i], lst[j] = lst[j], lst[i]

            left, right = i + 1, len(lst) - 1
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

            return True

        ret = []
        lst = sorted(s)
        ret.append("".join(lst))
        while nextPermutation(lst):
            ret.append("".join(lst))

        return ret

    def permutation2(self, s: str) -> List[str]:
        res = set()
        for item in itertools.permutations(s):
            res.add("".join(item))
        return list(res)
# leetcode submit region end(Prohibit modification and deletion)
