# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。 
# 
#  实现词典类 WordDictionary ： 
# 
#  
#  WordDictionary() 初始化词典对象 
#  void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配 
#  bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回 false 。word 中可能包含一些 
# '.' ，每个 . 都可以表示任何一个字母。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["WordDictionary","addWord","addWord","addWord","search","search","search",
# "search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
# 
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // 返回 False
# wordDictionary.search("bad"); // 返回 True
# wordDictionary.search(".ad"); // 返回 True
# wordDictionary.search("b.."); // 返回 True
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= word.length <= 25 
#  addWord 中的 word 由小写英文字母组成 
#  search 中的 word 由 '.' 或小写英文字母组成 
#  最多调用 10⁴ 次 addWord 和 search 
#  
# 
#  Related Topics 深度优先搜索 设计 字典树 字符串 👍 455 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class TrieNode:
#     def __init__(self):
#         self.children = [None for _ in range(26)]
#         self.isEnd = False
#
#     def add(self, word):
#         node = self
#         for ch in word:
#             if node.children[ord(ch) - ord('a')] is None:
#                 node.children[ord(ch) - ord('a')] = TrieNode()
#             node = node.children[ord(ch) - ord('a')]
#         node.isEnd = True


class WordDictionary:

    # def __init__(self):
    #     self.root = TrieNode()
    #
    # def addWord(self, word: str) -> None:
    #     self.root.add(word)
    #
    # def search(self, word: str) -> bool:
    #     def dfs(index: int, node: TrieNode) -> bool:
    #         if index == len(word):
    #             return node.isEnd
    #         ch = word[index]
    #         if ch != '.':
    #             child = node.children[ord(ch) - ord('a')]
    #             if child is not None and dfs(index+1, child):
    #                 return True
    #         else:
    #             for child in node.children:
    #                 if child is not None and dfs(index+1, child):
    #                     return True
    #
    #         return False
    #
    #     return dfs(0, self.root)
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
    #     self.dictw = {}
    #     self.dictn = defaultdict(list)
    #
    # def addWord(self, word: str) -> None:
    #     if word not in self.dictw:
    #         self.dictn[len(word)].append(word)
    #         self.dictw[word] = len(word)
    #
    # def search(self, word: str) -> bool:
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
    # 这种方法在leetcode英文站正确，在中文站报错，非常奇怪。
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

    # 下面这种方法超时了。但是在英文站可以
    # def __init__(self):
    #     self.children = [None] * 26
    #     self.isEnd = False
    #
    # def addWord(self, word: str) -> None:
    #     node = self
    #     for ch in word:
    #         order = ord(ch) - ord('a')
    #         if node.children[order] is None:
    #             node.children[order] = WordDictionary()
    #         node = node.children[order]
    #     node.isEnd = True
    #
    # def search(self, word: str) -> bool:
    #     node = self
    #     for i in range(len(word)):
    #         if word[i] == '.':
    #             for ch in node.children:
    #                 if ch is not None and ch.search(word[i + 1:]):
    #                     return True
    #             return False
    #         else:
    #             order = ord(word[i]) - ord('a')
    #             if node.children[order] is None:
    #                 return False
    #             node = node.children[order]
    #     return True if node.isEnd else False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# leetcode submit region end(Prohibit modification and deletion)
