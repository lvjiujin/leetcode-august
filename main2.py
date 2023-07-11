from typing import List


# class TrieNode:
#     def __init__(self):
#         self.children = [ None for _ in range(26)]
#         self.isWord = False


def replaceWords(dictionary: List[str], sentence: str) -> str:
    def buildTrie(dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if node.children[ord(ch) - ord('a')] is None:
                    node.children[ord(ch) - ord('a')] = TrieNode()
                node = node.children[ord(ch) - ord('a')]
            node.isWord = True

        return root

    def findWord(root, word):
        node = root
        ch_lst = []
        for ch in word:
            if node.isWord or node.children[ord(ch) - ord('a')] is None:
                break
            ch_lst.append(ch)
            node = node.children[ord(ch) - ord('a')]
        return "".join(ch_lst) if node.isWord else ""

    root = buildTrie(dictionary)
    words = sentence.split(" ")
    for i in range(len(words)):
        prefix = findWord(root, words[i])
        if prefix != "":
            words[i] = prefix
    return " ".join(words)


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __hash__(self):
        return hash((self.val, self.left, self.right))  # get a tuple's hash

    def __eq__(self, other):
        return (self.val, self.left, self.right) == (other.val, other.left, other.right)


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        parent = dict()
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]

        return q

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 二分查找：
        if nums[0] >= target:
            return []
        i, j = 0, len(nums) - 1

        for i in range(len(nums)):
            temp = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left ) // 2
                if temp < nums[mid]:
                    right = mid - 1
                elif temp > nums[mid]:
                    left = mid + 1
                else:
                    return [i, mid]
        return []

    def permutation(self, s: str) -> List[str]:

        def nextPermutation(lst) -> bool:
            """
            Do not return anything, modify nums in-place instead.
            从后往前寻找非降序的a[i-1], 寻找a[j]，满足:a[i-1] < a[j],
            交换a[i-1]和a[j]，反转a[i-]之后的元素
            """

            i = len(lst) - 2
            while i >= 0 and lst[i] >= lst[i + 1]:
                i -= 1
            if i < 0:
                print(" i < 0")
                return False
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
        k = 0
        lst = sorted(s)
        print("lst = ", lst)
        ret.append("".join(lst))
        while nextPermutation(lst):
            k += 1
            if k > 10:
                break
            print("lst = ", lst)
            ret.append("".join(lst))

        return ret

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def buildGraph(equations, values):
            size = len(equations)
            graph = dict()
            for i in range(size):
                var1 = equations[i][0]
                var2 = equations[i][1]
                temp1 = dict()
                temp1[var2] = values[i]
                graph[var1] = temp1
                temp2 = dict()
                temp2[var1] = 1/values[i]
                graph[var2] = temp2
            print("graph = ", graph)
            return graph

        graph = buildGraph(equations, values)


        def dfs(graph, begin, end, visited):
            if begin == end:
                return 1.0
            visited.add(begin[:])
            for nxt in graph[begin]:
                if nxt not in visited:
                    nxtValue = dfs(graph, nxt, end, visited)
                    if nxtValue > 0:
                        return graph[begin][nxt] * nxtValue
            visited.remove(begin)
            return -1.0

        size = len(queries)
        result = [0.0 for _ in range(size)]
        # print("size = ", size)
        for i in range(size):
            begin = queries[i][0]
            end = queries[i][1]
            if begin not in graph or end not in graph:
                result[i] = -1.0
            else:
                visited = set()
                result[i] = dfs(graph, begin, end, visited)

        return result

    def findMaximumXOR(self, nums: List[int]) -> int:
        class TrieNode:
            def __init__(self):
                self.children = [None for _ in range(2)]

        root = TrieNode()
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                # print("bit = ", bit)
                if node.children[bit] is None:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        max_res = 0
        for num in nums:
            node = root
            xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1

                if node.children[1 - bit] is not None:
                    xor = xor *2 + 1
                    node = node.children[1 - bit]
                else:
                    xor = xor * 2
                    node = node.children[bit]

            max_res = max(max_res, xor)
        return max_res


def main():
    pass
    # words = ["cat", "bat", "rat"]
    # sents = "the cattle was rattled by the battery"
    # # the cat was rat by the bat
    # # the cat was rat b the bat
    # print("words = ", words)
    # print("sents = ", sents)
    # new_sents = replaceWords(words, sents)
    # print(new_sents)
    # word = "hello"
    # for i in range(len(word)-1, -1, -1):
    #     ch = word[i]
    #     print("ch = ", ch)
    # nums = [10, 100]
    # solution = Solution()
    # res = solution.findMaximumXOR(nums)
    # print("res = ", res)

    # equations = [["a", "b"], ["b", "c"]]
    # values = [2.0, 3.0]
    # queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    # solution = Solution()
    # res = solution.calcEquation(equations, values, queries)
    # print('res =', res)
    solution = Solution()
    # s = "abc"
    # res = solution.permutation(s)
    # print("res = ", res)
    # res = solution.twoSum([2,7,11,15], 9)
    # print("res = ", res)

    root = {val: 3, left: TreeNode{val: 5, left: TreeNode{val: 6, left: None, right: None}, right: TreeNode
    {val: 2, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode
    {val: 4, left: None, right: None}}}, right: TreeNode
    {val: 1, left: TreeNode{val: 0, left: None, right: None}, right: TreeNode
    {val: 8, left: None, right: None}}}
    solution = solution.lowestCommonAncestor(root, p, q)


main()
