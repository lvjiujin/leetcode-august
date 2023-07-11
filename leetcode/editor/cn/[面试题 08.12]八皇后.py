# 设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整
# 个棋盘的那两条对角线。 
# 
#  注意：本题相对原题做了扩展 
# 
#  示例: 
# 
#   输入：4
#  输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#  解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#  
# 
#  Related Topics 数组 回溯 👍 168 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def dfs(n, row, col, pie, na, path):
            if row == n:
                result.append(["." * v + "Q" + (n - 1 - v) * "." for v in path])

            pos = ~(col | pie |na) & ((1 << n) -1)
            while pos:
                p = pos&(-pos)
                pos = pos & (pos -1)
                v = bin(p-1).count('1')
                dfs(n, row + 1, col | p, (pie| p) << 1, (na|p) >> 1, path + [v])
        dfs(n, 0, 0, 0, 0, [])
        return resultsh

    def solveNQueens2(self, n: int) -> List[List[str]]:
        if n <= 0:
            return []
        chessboard = [['.'] * n for _ in range(n)]
        result = []
        def isValid(row, col, chessboard):
            for i in range(row):
                if chessboard[i][col] == 'Q':
                    return False
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if chessboard[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if chessboard[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def backTracking(chessboard, row, n):
            if row == n:
                result.append(["".join(x) for x in chessboard])
            for col in range(n):
                if not isValid(row, col, chessboard):
                    continue
                chessboard[row][col] = 'Q'
                backTracking(chessboard, row + 1, n)
                chessboard[row][col] = '.'

        backTracking(chessboard, 0, n)
        return result


# leetcode submit region end(Prohibit modification and deletion)
