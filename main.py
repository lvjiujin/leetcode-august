# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

"""
nonlocal只能在封装函数中使用，在外部函数先进行声明，在内部函数进行nonlocal声明，
这样在func()函数中的x与subfunc()中的x是同一个变量。
"""

def func():
    x = 2
    def subfunc(num):
        nonlocal x # nonlocal是用于函数中的函数
        x = x + num

    subfunc(2)
    print("x = ", x)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4 :
            return []
        n = len(nums)
        nums.sort()
        print("sorted nums = ", nums)
        result = []

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                partsum = nums[i] + nums[j]
                left, right = j+1, n-1
                while left < right:
                    s = partsum + nums[left] + nums[right]
                    if s == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right:
                            left += 1
                            if nums[left] != nums[left-1]:
                                break
                        while left < right:
                            right -= 1
                            if nums[right] != nums[right+1]:
                                break
                    elif s > target:
                        right-=1
                        while left < right and  nums[right] == nums[right+1]:
                            right-=1
                    else:
                        left+=1
                        while left < right and  nums[left] == nums[left-1]:
                            left+=1

        return result

    def get_next(self, P):
        # get_next是统计出每个位置之前的子串的前后缀数目
        n = len(P)
        nxt = [0] * (n+1)
        nxt[0] = -1  # nxt[0]的这个位置，相当于是一个标志。
        i, j = 0, -1
        while i < n:
            if j == -1 or P[i] == P[j]:
                i, j = i+1, j+1
                nxt[i] = j
            else:
                j = nxt[j]

        return nxt


    def generateNext(self, p: str):
        """
        生成 next 数组
        next[j] 表示下标 j 之前的模式串 p 中，最长相等前后缀的长度
        :param p:
        :return:
        """
        m = len(p)
        next = [0 for _ in range(m)]  # 初始化数组元素全部为 0

        left = 0  # left 表示前缀串开始所在的下标位置
        for right in range(1, m):  # right 表示后缀串开始所在的下标位置
            while left > 0 and p[left] != p[right]:  # 匹配不成功, left 进行回退, left == 0 时停止回退
                left = next[left - 1]  # left 进行回退操作
            if p[left] == p[right]:  # 匹配成功，找到相同的前后缀，先让 left += 1，此时 left 为前缀长度
                left += 1
            next[right] = left  # 记录前缀长度，更新 next[right], 结束本次循环, right += 1

        return next

    # KMP 匹配算法，T 为文本串，p 为模式串
    def kmp(self, T: str, p: str) -> int:
        n, m = len(T), len(p)

        next = self.generateNext(p)  # 生成 next 数组
        j = 0  # j 为模式串中当前匹配的位置
        for i in range(n):  # i 为文本串中当前匹配的位置
            while j > 0 and T[i] != p[j]:  # 如果模式串前缀匹配不成功, 将模式串进行回退, j == 0 时停止回退
                j = next[j - 1]
            if T[i] == p[j]:  # 当前模式串前缀匹配成功，令 j += 1，继续匹配
                j += 1
            if j == m:  # 当前模式串完全匹配成功，返回匹配开始位置
                return i - j + 1
        return -1  # 匹配失败，返回 -1

    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s:
        #     return 0
        # ss = ""
        # res = []
        # for x in s:
        #     if x not in ss:
        #         ss += x
        #         res.append(ss)
        #
        #     else:
        #
        #         index = ss.find(x)
        #         ss = ss[index+1:] + x
        #
        # return max([len(x) for x in res])
        # 滑动窗口法：
        # 当没有重复字符时调整右边界，有重复字符时调整左边界
        if not s:
            return 0
        freq = {}
        start = max_length = 0
        for end, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1
            while freq[c] > 1:
                freq[s[start]] -=1 # 懂了，这里是将start对应字符的计数减一，而不是freq[c]-1. 用循环的目的是可以减少到freq[c]=1
                start+=1
            max_length = max(max_length, end-start + 1)
        return max_length

    def reverseWords(self, s: str) -> str:
        if not s:
            return ''
        s = s.strip()
        return " ".join([x.strip() for x in s.split(" ") if x != ""][::-1])

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        # 方法一：
        ans = "0"
        m, n = len(num1), len(num2)
        for i in range(n - 1, -1, -1):
            add = 0
            y = int(num2[i])
            curr = ["0"] * (n - i - 1)
            for j in range(m - 1, -1, -1):
                product = int(num1[j]) * y + add
                curr.append(str(product % 10))
                add = product // 10
            if add > 0:
                curr.append(str(add))
            curr = "".join(curr[::-1])
            ans = self.addStrings(ans, curr)

        return ans

        # 方法二：
        # m, n = len(num1), len(num2)
        # ansArr = [0] * (m + n)
        # for i in range(m - 1, -1, -1):
        #     x = int(num1[i])
        #     for j in range(n - 1, -1, -1):
        #         ansArr[i + j + 1] += x * int(num2[j])
        #
        # for i in range(m + n - 1, 0, -1):
        #     ansArr[i - 1] += ansArr[i] // 10
        #     ansArr[i] %= 10
        #
        # index = 1 if ansArr[0] == 0 else 0
        # ans = "".join(str(x) for x in ansArr[index:])
        # return ans

    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) -1
        carry = 0
        ans = ""
        while i >= 0 or j >= 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >=0 else 0
            temp = x + y + carry
            carry = temp // 10
            ans = str(temp % 10) + ans
            i -= 1
            j -= 1
        return ans if not carry else '1' + ans




if __name__ == '__main__':
    # func()
    solution = Solution()
    # s = "ABCABCD"
    # s = "ABCABCABC"
    # # next = solution.generateNext(s)
    # nxt = solution.get_next(s)
    # print("next = ", nxt)
    # nums = [-2, -1, -1, 1, 1, 2, 2]
    # target = 0

    # res = solution.fourSum(nums, target)
    # print("res = ", res)
    # print("正确结果为：[[-2,-1,1,2],[-1,-1,1,1]]")

    # s = "pwwkew"
    # length = solution.lengthOfLongestSubstring(s)
    # print("length = ", length)
    # s = "a good   example"
    # res = solution.reverseWords(s)
    # print("res = ", res)
    num1 = "1234"
    num2 = "567"
    res = solution.multiply(num1, num2)
    print("res = ", res)

