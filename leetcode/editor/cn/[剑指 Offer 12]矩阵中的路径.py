# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = 
# "ABCCED"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n = board[i].length 
#  1 <= m, n <= 6 
#  1 <= word.length <= 15 
#  board 和 word 仅由大小写英文字母组成 
#  
# 
#  注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/ 
# 
#  Related Topics 数组 回溯 矩阵 👍 694 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

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
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(x, y, length, visited):
            if len(word) == length:
                return True
            hasPath = False

            if 0 <= x < m and 0 <= y < n and board[x][y] == word[length] and not visited[x][y]:
                length += 1
                visited[x][y] = True

                hasPath = dfs(x + 1, y, length, visited) or \
                          dfs(x - 1, y, length, visited) or \
                          dfs(x, y - 1, length, visited) or \
                          dfs(x, y + 1, length, visited)
                if not hasPath:
                    length -= 1
                    visited[x][y] = False

            return hasPath

        visited = [[False] * n for _ in range(m)]
        pathLength = 0
        for i in range(m):
            for j in range(n):
                if dfs(i, j, pathLength, visited):
                    return True

        return False

# leetcode submit region end(Prohibit modification and deletion)
