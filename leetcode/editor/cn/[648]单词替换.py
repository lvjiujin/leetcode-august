# 在英语中，我们有一个叫做 词根(root) 的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词
# 根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。 
# 
#  现在，给定一个由许多词根组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。你需要将句子中的所有继承词用词根替换掉。如果继
# 承词有许多可以形成它的词根，则用最短的词根替换它。 
# 
#  你需要输出替换之后的句子。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by 
# the battery"
# 输出："the cat was rat by the bat"
#  
# 
#  示例 2： 
# 
#  
# 输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# 输出："a a b c"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= dictionary.length <= 1000 
#  1 <= dictionary[i].length <= 100 
#  dictionary[i] 仅由小写字母组成。 
#  1 <= sentence.length <= 10^6 
#  sentence 仅由小写字母和空格组成。 
#  sentence 中单词的总量在范围 [1, 1000] 内。 
#  sentence 中每个单词的长度在范围 [1, 1000] 内。 
#  sentence 中单词之间由一个空格隔开。 
#  sentence 没有前导或尾随空格。 
#  
# 
#  
# 
#  Related Topics 字典树 数组 哈希表 字符串 👍 251 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:


    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class TrieNode:
            def __init__(self):
                self.children = dict()
                self.isWord = False
        def buildTrie(dictionary):
            root = TrieNode()
            for word in dictionary:
                node = root
                for ch in word:
                    if ch not in node.children:
                        node.children[ch] = TrieNode()
                    node = node.children[ch]
                node.isWord = True

            return root

        def findWord(root, word):
            node = root
            ch_lst = []
            for ch in word:
                if node.isWord or ch not in node.children:
                    break
                ch_lst.append(ch)
                node = node.children[ch]
            return "".join(ch_lst) if node.isWord else ""

        root = buildTrie(dictionary)
        words = sentence.split(" ")
        for i in range(len(words)):
            prefix = findWord(root, words[i])
            if prefix != "":
                words[i] = prefix
        return " ".join(words)

    def replaceWords2(self, dictionary: List[str], sentence: str) -> str:
        # 首先将 dictionary 中所有词根放入哈希集合中，然后对于 sentence中的每个单词，
        # 由短至长遍历它所有的前缀，如果这个前缀出现在哈希集合中，则我们找到了当前单词的最短词根，
        # 将这个词根替换原来的单词。最后返回重新拼接的句子。

        dict_set = set(dictionary)
        words = sentence.split(' ')
        for i, word in enumerate(words):
            for j in range(1, len(word)):
                if word[:j] in dict_set:
                    words[i] = word[:j]
                    break
        return ' '.join(words)


    def replaceWords3(self, dictionary: List[str], sentence: str) -> str:
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

# leetcode submit region end(Prohibit modification and deletion)
