# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。 
# 
# 
#  你可以 任意多次交换 在 pairs 中任意一对索引处的字符。 
# 
#  返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。 
# 
#  
# 
#  示例 1: 
# 
#  输入：s = "dcab", pairs = [[0,3],[1,2]]
# 输出："bacd"
# 解释： 
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"
#  
# 
#  示例 2： 
# 
#  输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# 输出："abcd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[0] 和 s[2], s = "acbd"
# 交换 s[1] 和 s[2], s = "abcd" 
# 
#  示例 3： 
# 
#  输入：s = "cba", pairs = [[0,1],[1,2]]
# 输出："abc"
# 解释：
# 交换 s[0] 和 s[1], s = "bca"
# 交换 s[1] 和 s[2], s = "bac"
# 交换 s[0] 和 s[1], s = "abc"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  0 <= pairs.length <= 10^5 
#  0 <= pairs[i][0], pairs[i][1] < s.length 
#  s 中只含有小写英文字母 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 哈希表 字符串 👍 284 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    class UnionFind:

        def __init__(self, N):
            # 初始化,parent[i] =i 祖先的祖先是自己。
            self.parent = [i for i in range(N)]
            self.rank = [1 for _ in range(N)]

        def find(self, index):
            if self.parent[index] == index:
                return index
            # 递归，不断向上查找其祖先。
            self.parent[index] = self.find(self.parent[index])

            return self.parent[index]

        def union(self, index1, index2):
            root1 = self.find(index1)
            root2 = self.find(index2)
            if root1 == root2:
                return

            if self.rank[root1] == self.rank[root2]:
                self.parent[root1] = root2
                self.rank[root2] += 1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
        # 方法一：并查集
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        if len(pairs) == 0:
            return s
        # 第一步：将任意交换的节点对输入并查集
        n = len(s)
        uf = Solution.UnionFind(n)
        for x, y in pairs:
            uf.union(x, y)
        # 第二步：遍历输入字符串 s，对于每一个索引，找到这个索引在并查集中的代表元
        # 把同属于一个代表元的字符放在一起。这一步需要建立一个映射关系。
        import collections
        mp = collections.defaultdict(list)
        for i, ch in enumerate(s):
            mp[uf.find(i)].append(ch)
        # 第三步：分组排序。即对同属于一个连通分量中的字符进行排序
        for vec in mp.values():
            vec.sort(reverse=True)

        ans = list()
        for i in range(len(s)):
            x = uf.find(i)
            ans.append(mp[x][-1])
            mp[x].pop()

        return "".join(ans)

    # 方法二：dfs

    # def dfs(self, res, graph, visited, x):
    #     for neighbor in graph[x]:
    #         if not visited[neighbor]:
    #             visited[neighbor] = 1
    #             res.append(neighbor)
    #             self.dfs(res, graph, visited, neighbor)
    #
    # def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    #     # 建图
    #     graph = [[] for _ in range(len(s))]
    #     visited = [0] * len(s)
    #     for x, y in pairs:
    #         graph[x].append(y)
    #         graph[y].append(x)
    #
    #     res = list(s)
    #     for i in range(len(s)):
    #         if not visited[i]:
    #             # 获取连通节点
    #             connected_nodes = []
    #             self.dfs(connected_nodes, graph, visited, i)
    #             # 重新赋值
    #             indices = sorted(connected_nodes)
    #             string = sorted(res[node] for node in connected_nodes)
    #             for j, ch in zip(indices, string):
    #                 res[j] = ch
    #
    #     return "".join(res)

    # 方法三：BFS
    # def bfs(self, res, graph, visited, x):
    #     queue = collections.deque([x])
    #     visited[x] = 1
    #     res.append(x)
    #
    #     while queue:
    #         cur_node = queue.popleft()
    #         for neighbor in graph[cur_node]:
    #             if visited[neighbor]:
    #                 continue
    #             visited[neighbor] = 1
    #             res.append(neighbor)
    #             queue.append(neighbor)
    #
    # def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    #     # 建图
    #     graph = [[] for _ in range(len(s))]
    #     visited = [0] * len(s)
    #     for x, y in pairs:
    #         graph[x].append(y)
    #         graph[y].append(x)
    #
    #     res = list(s)
    #     for i in range(len(s)):
    #         if not visited[i]:
    #             # 获取联通节点
    #             connected_nodes = []
    #             self.bfs(connected_nodes, graph, visited, i)
    #             # 重新赋值
    #             indices = sorted(connected_nodes)
    #             string = sorted(res[node] for node in connected_nodes)
    #             for j, ch in zip(indices, string):
    #                 res[j] = ch
    #
    #     return "".join(res)






# leetcode submit region end(Prohibit modification and deletion)
