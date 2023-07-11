# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。 
# 
#  单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使
# 用。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f",
# "l","v"]], words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#  
# 
#  示例 2： 
#  
#  
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 12 
#  board[i][j] 是一个小写英文字母 
#  1 <= words.length <= 3 * 10⁴ 
#  1 <= words[i].length <= 10 
#  words[i] 由小写英文字母组成 
#  words 中的所有字符串互不相同 
#  
# 
#  Related Topics 字典树 数组 字符串 回溯 矩阵 👍 719 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

import collections

class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.word = ""
        self.isEnd = False

    def insert(self, word: str) -> None:
        cur = self
        for ch in word:
            cur = cur.children[ch]
        cur.isEnd = True
        cur.word = word

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = list()
        m, n = len(board), len(board[0])

        def dfs(node, x, y):
            ch = board[x][y]
            if ch not in node.children: # board[x][y]不在trie树中，直接返回
                return
            nxt = node.children[ch]
            if nxt.word != "":
                ans.append(nxt.word)
                nxt.word = ""
            if nxt.children:
                board[x][y] = '#'
                for xi, yi in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= xi < m and 0 <= yi < n:
                        dfs(nxt, xi, yi)
                board[x][y] = ch
            else:
                node.children.pop(ch)

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return ans

    def findWords1(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = set()
        m, n = len(board), len(board[0])

        def dfs(node, x, y):
            ch = board[x][y]
            if ch not in node.children: # board[x][y]不在trie树中，直接返回
                return
            node = node.children[ch]
            if node.word != "":
                ans.add(node.word)
            board[x][y] = '#'
            for xi, yi in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= xi < m and 0 <= yi < n:
                    dfs(node, xi, yi)
            board[x][y] = ch

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return list(ans)


# leetcode submit region end(Prohibit modification and deletion)
