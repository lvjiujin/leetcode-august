# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。 
# 
#  n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。 
# 
#  
#  
#  每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
#  
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[["Q"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  
# 
#  Related Topics 数组 回溯 👍 1543 👎 0

import itertools
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 基于位运算的回溯
    def solveNQueens4(self, n: int) -> List[List[str]]:

        solutions = list()
        queens = [-1] * n  # 这个数组用于记录每行中皇后所在的位置
        row = ["."] * n

        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def solve(row: int, columns: int, diagonals1: int, diagonals2: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while availablePositions:
                    position = availablePositions & (-availablePositions)
                    availablePositions = availablePositions & (availablePositions - 1)
                    column = bin(position - 1).count("1")
                    queens[row] = column
                    solve(row + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1)

        solve(0, 0, 0, 0)
        return solutions

    def solveNQueens1(self, n: int):
        return [['.' * v + 'Q' + '.' * (n - 1 - v) for v in p]
                for p in itertools.permutations(list(range(n)))
                if len(set([v - i for i, v in enumerate(p)])) ==
                len(set([v + i for i, v in enumerate(p)])) == n]

    def solveNQueens3(self, n: int) -> List[List[str]]:

        def backtrack(r, columns, diagonal1, diagonal2, path):
            if r == n:
                print("path = ", path)
                return [['.' * v + 'Q' + '.' * (n - 1 - v) for v in path]]
            c = []
            for i in range(n):
                # i 代表列, r代表行。
                # 当前列及正反对角线都没有皇后时；再进行放置皇后
                if i in columns or r - i in diagonal1 or r + i in diagonal2:
                    continue
                c += backtrack(r + 1, columns + [i], diagonal1 + [r - i], diagonal2 + [r + i], path + [i])
            return c

        return backtrack(0, [], [], [], [])

    def solveNQueens5(self, n: int) -> List[List[str]]:
        if not n:
            return []
        chessboard = [['.'] * n for _ in range(n)]
        res = []

        def isVaild(chessboard, row, col):
            # 因为我们是从上往下放置皇后的；只用判断当前行之前的就行；之后的我们还没有放置，不用判断。
            # 当前行之前就三个方向，同一列，左上角对角线，右上角对角线。
            # 判断同一列是否冲突
            for i in range(row):
                if chessboard[i][col] == 'Q':
                    return False
            # 判断左上角是否冲突
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if chessboard[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # 判断右上角是否冲突
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(chessboard):
                if chessboard[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtracking(chessboard, row, n):
            # 如果走到最后一行，说明已经找到一个解
            if row == n:
                res.append([''.join(x) for x in chessboard])
            for col in range(n):
                if not isVaild(chessboard, row, col):
                    continue
                chessboard[row][col] = 'Q'
                backtracking(chessboard, row + 1, n)
                chessboard[row][col] = '.'

        backtracking(chessboard, 0, n)
        return res

    def solveNQueens2(self, n: int) -> List[List[str]]:

        result = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n

        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                result.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        backtrack(0)
        return result

    def solveNQueens(self, n: int) -> List[List[str]]:
        # 两个二进制的位运算要掌握牢记:
        # x & (x -1) 保留x中最后一位1
        # x & (-x) 把x中最后一位1置0
        # 后序研究二进制的N皇后问题。
        result = []

        def dfs(n, row, col, pie, na, path):
            # pie, na分别是两个不同方向的对角线，和汉字笔画的方向对应。

            if row == n:  # 当行数 遍历完，就结束了。
                result.append(['.' * v + 'Q' + '.' * (n - 1 - v) for v in path])

            # pos 中的1表示可以放置皇后的位置。
            # col | pie | na表示不能放置皇后的位置，取反变成可以放置皇后的位置，&((1<<n)-1)只保留最后n个位置。前面(32-n)消除掉。
            pos = ~(col | pie | na) & ((1 << n) - 1)
            while pos:  # pos 不为0，说明还有位置可以放置皇后，还可以继续递归。'1'即可以放皇后的位置
                p = pos & (-pos)  # 将pos中最右边的1保留在p中，其余位置变为0.
                pos &= (pos - 1)  # 将pos中最右边的1变为0
                v = bin(p - 1).count('1') # 获取每一行中皇后列的位置
                # row + 1,继续下一行
                # col | p 即放了皇后的位置对列的影响，或的关系，就是二者叠加。
                # (pie | p )  放了皇后的位置对pie的影响，因为行号向下移动一行，所以pie(左对角线）要向下平移(<<1，左移1位）
                # (na |p)放了皇后的位置对na的影响，因为行号向下移动一行(row + 1),所以na(右对角线）要向下平移(>>1,右移1位）
                dfs(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1, path + [v])

        dfs(n, 0, 0, 0, 0, [])
        return result

# leetcode submit region end(Prohibit modification and deletion)
