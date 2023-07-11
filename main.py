# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
from collections import defaultdict

"""
nonlocal只能在封装函数中使用，在外部函数先进行声明，在内部函数进行nonlocal声明，
这样在func()函数中的x与subfunc()中的x是同一个变量。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def func():
    x = 2

    def subfunc(num):
        nonlocal x  # nonlocal是用于函数中的函数
        x = x + num

    subfunc(2)
    print("x = ", x)


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        # 这个代码要好好理解下
        charToCount = dict()
        # 首先统计字符串t中字符的词频，放到hash 字典 charToCount中。
        for ch in t:
            charToCount[ch] = charToCount.get(ch, 0) + 1
        # count表示t中一共有多少个不同的字符。
        count = len(charToCount)
        start, end, minStart, minEnd = [0, 0, 0, 0]
        shortest = 10 ** 5 + 1  # 字符串最大长度为10**5,所以这里这样初始化。
        while end < len(s) or (count == 0 and end == len(s)):
            if count > 0:
                endCh = s[end]
                if endCh in charToCount:
                    charToCount[endCh] = charToCount.get(endCh) - 1
                    if charToCount.get(endCh) == 0:  # 说明s中有该字符（即含有t中的字符)
                        count -= 1

                end += 1  # 右指针继续往右移动，判断s中的下一个字符。
            else:
                # else 是count ==0 说明此时, 从start到end之间的字符串已经包含了t串。因为要寻找最短子串，于是start向右转移。
                if end - start < shortest:
                    shortest = end - start
                    minStart = start
                    minEnd = end

                startCh = s[start]
                if startCh in charToCount:
                    charToCount[startCh] = charToCount.get(startCh) + 1
                    if charToCount[startCh] == 1:
                        count += 1

                start += 1

        return s[minStart:minEnd] if shortest < (10 ** 5 + 1) else ""

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        n = len(nums)
        nums.sort()
        print("sorted nums = ", nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                partsum = nums[i] + nums[j]
                left, right = j + 1, n - 1
                while left < right:
                    s = partsum + nums[left] + nums[right]
                    if s == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right:
                            left += 1
                            if nums[left] != nums[left - 1]:
                                break
                        while left < right:
                            right -= 1
                            if nums[right] != nums[right + 1]:
                                break
                    elif s > target:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    else:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

        return result

    def get_next(self, P):
        # get_next是统计出每个位置之前的子串的前后缀数目
        n = len(P)
        nxt = [0] * (n + 1)
        nxt[0] = -1  # nxt[0]的这个位置，相当于是一个标志。
        i, j = 0, -1
        while i < n:
            if j == -1 or P[i] == P[j]:
                i, j = i + 1, j + 1
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
                freq[s[start]] -= 1  # 懂了，这里是将start对应字符的计数减一，而不是freq[c]-1. 用循环的目的是可以减少到freq[c]=1
                start += 1
            max_length = max(max_length, end - start + 1)
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
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        ans = ""
        while i >= 0 or j >= 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            temp = x + y + carry
            carry = temp // 10
            ans = str(temp % 10) + ans
            i -= 1
            j -= 1
        return ans if not carry else '1' + ans

    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     # 二叉树的层序遍历，每一层都是一个对称数组，只有这样才满足对称二叉树。
    #     if not root:
    #         return []
    #     queue = [root]
    #     while queue:
    #         # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数,不在同一层的就不会同时出现在队列中。
    #         size = len(queue)
    #         tmp = []
    #         # 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
    #         # 如果节点的左/右子树不为空，也放入队列中
    #         for _ in range(size):
    #             r = queue.pop(0)
    #             tmp.append(r.val)
    #             if r.left:
    #                 queue.append(r.left)
    #             if r.right:
    #                 queue.append(r.right)
    #         # 将临时list加入最终返回结果中
    #         for i in range(len(tmp)):
    #             if tmp[i] != tmp[len(tmp) - 1 - i]:
    #                 return False
    #
    #     return True

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # 首先将 dictionary 中所有词根放入哈希集合中，然后对于 sentence中的每个单词，
        # 由短至长遍历它所有的前缀，如果这个前缀出现在哈希集合中，则我们找到了当前单词的最短词根，
        # 将这个词根替换原来的单词。最后返回重新拼接的句子。

        # dict_set = set(dictionary)
        # words = sentence.split(' ')
        # for i, word in enumerate(words):
        #     for j in range(1, len(word)):
        #         if word[:j] in dict_set:
        #             words[i] = word[:j]
        #             break
        # return ' '.join(words)
        trie = {}
        for word in dictionary:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = {}
        print("trie = ", trie)
        """
        ["cat", "bat", "rat"]
        trie =  {'c': {'a': {'t': {'#': {}}}}, 
                'b': {'a': {'t': {'#': {}}}}, 
                'r': {'a': {'t': {'#': {}}}}} 
        """
        words = sentence.split(' ')
        for i, word in enumerate(words):
            cur = trie
            for j, c in enumerate(word):
                if '#' in cur:
                    words[i] = word[:j]
                    break
                if c not in cur:
                    break
                cur = cur[c]
        return ' '.join(words)


class WordDictionary:
    def __init__(self):
        self.dct = dict()

    def addWord(self, word: str) -> None:
        cur = self.dct
        for w in word:
            if w not in cur:
                cur[w] = dict()
            cur = cur[w]
        cur['isEnd'] = 1
        return

    def search(self, word: str) -> bool:

        def dfs(cur, i):
            nonlocal ans
            if i == n:
                if 'isEnd' in cur:
                    ans = True
                return
            if ans:
                return
            if word[i] == '.':
                for w in cur:
                    if w != 'isEnd':
                        dfs(cur[w], i + 1)
            if word[i] in cur:
                dfs(cur[word[i]], i + 1)
            return

        n = len(word)
        ans = False
        dfs(self.dct, 0)
        return ans

    # def __init__(self):
    #     self.dictw = dict()
    #     self.dictn = defaultdict(list)
    #
    # def addWord(self, word: str) -> None:
    #     if word not in self.dictw:
    #         self.dictn[len(word)].append(word)
    #         self.dictw[word] = len(word)
    #
    # def search(self, word: str) -> bool:
    #     print("word = ", word)
    #     if word in self.dictw:
    #         return True
    #     # 双dict，长度和字符互相为key，直接比较，完美
    #     for w in self.dictn[len(word)]:
    #         if '.' in word:
    #             length = 0
    #             for i in range(len(w)):
    #                 if w[i] == word[i] or word[i] == '.':
    #                     length += 1
    #                 else:
    #                     break
    #             if length == len(w):
    #                 return True
    #     return False
    # def __init__(self):
    #     self.trie = {}
    #
    # def addWord(self, word):  # e.g., root -> [s] -> [e] -> [a] -> ['$']
    #     node = self.trie
    #     for char in word:
    #         if char not in node:
    #             node[char] = {}
    #         node = node[char]
    #     node['$'] = None  # end of word
    #
    # def search(self, word):
    #     n = len(word)
    #
    #     def dfs(node, char_index=0):  # e.g., char_index, 0, 1, 2: [s] (0) -> [e] (1) -> [a] (2)
    #         if char_index == n:
    #             return '$' in node
    #         if word[char_index] == ".":
    #             for letter in node:
    #                 if letter != '$' and dfs(node[letter], char_index + 1):
    #                     return True
    #         elif word[char_index] in node:
    #             return dfs(node[word[char_index]], char_index + 1)
    #         else:
    #             return False
    #
    #     return dfs(self.trie)


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
    # num1 = "1234"
    # num2 = "567"
    # res = solution.multiply(num1, num2)
    # print("res = ", res)
    # dictionary = ["cat", "bat", "rat"]
    # sentence = "the cattle was rattled by the battery"
    # res = solution.replaceWords(dictionary, sentence)
    # print("res = ", res)
    # dictionary = ["WordDictionary", "addWord", "addWord", "search", "search", "search",
    #               "search", "search", "search"]
    # words = [[], ["a"], ["a"], ["."], ["a"], ["aa"], ["a"], [".a"], ["a."]]
    # word_dict = WordDictionary()
    # for word in dictionary:
    #     word_dict.addWord(word)
    #
    # res = word_dict.search('.')
    # print('res = ', res)
    # res = []
    # for word in words:
    #     if len(word) != 0:
    #         temp = word[0]
    #     else:
    #         temp = ""
    #     result = word_dict.search(temp)
    #     res.append(result)
    # print("res = ", res)

    import os

    # path = "C:\\Introduction_to_Algorithm_Training_Camp\\cpp_stl"
    # for file in os.listdir(path):
    #     new_file = "".join(file.split(' '))
    #     os.rename(os.path.join(path, file), os.path.join(path,new_file))

    # s = "ADOBECODEBANC"
    # t = "ABC"
    # # 测试结果: "BANC"
    # # 期望结果: "BANC"
    # res = solution.minWindow(s, t)
    # print('res = ', res)

