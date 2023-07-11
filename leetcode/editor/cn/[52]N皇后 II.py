# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
#  
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
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
#  Related Topics 回溯 👍 401 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def totalNQueens2(self, n: int) -> int:
        result = 0
        chessboard = [["."] * n for _ in range(n)]

        def isValid(row, col, chessboard):
            for i in range(row):
                if chessboard[i][col] == 'Q':
                    return False

            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if chessboard[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if chessboard[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True

        def backtracking(row, chessboard):
            nonlocal result
            if row == n:
                result += 1
            for i in range(n):
                if isValid(row, i, chessboard):
                    chessboard[row][i] = 'Q'
                    backtracking(row + 1, chessboard)
                    chessboard[row][i] = '.'

        backtracking(0, chessboard)
        return result

    def totalNQueens(self, n: int) -> int:
        # 两个二进制的位运算要掌握牢记:
        # x & (x -1) 保留x中最后一位1
        # x & (-x) 把x中最后一位1置0

        ans = 0

        def dfs(n, row, col, pie, na):
            # pie, na分别是两个不同方向的对角线，和汉字笔画的方向对应。

            nonlocal ans
            if row == n:  # 当行数 遍历完，就结束了。
                ans += 1
                return
            # pos 中的1表示可以放置皇后的位置。
            # col | pie | na表示不能放置皇后的位置，取反变成可以放置皇后的位置，&((1<<n)-1)只保留最后n个位置。前面(32-n)消除掉。
            pos = ~(col | pie | na) & ((1 << n) - 1)
            while pos != 0:  # pos 不为0，说明还有位置可以放置皇后，还可以继续递归。
                p = pos & (-pos)  # 将pos中最后一位1（最低位的1）置为0，也就是这个为了放了皇后.
                pos &= (pos - 1)  # 将pos中最后一位1保留到pos中，即将皇后位置保存在pos中。
                # row + 1,继续下一行
                # col | p 即放了皇后的位置对列的影响，或的关系，就是二者叠加。
                # (pie | p )  放了皇后的位置对pie的影响，因为行号向下移动一行，所以pie(左对角线）要向下平移(<<1，左移1位）
                # (na |p)放了皇后的位置对na的影响，因为行号向下移动一行(row + 1),所以na(右对角线）要向下平移(>>1,右移1位）
                dfs(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1)

        dfs(n, 0, 0, 0, 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
