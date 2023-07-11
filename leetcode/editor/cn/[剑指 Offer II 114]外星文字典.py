# 现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。 
# 
#  给定一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。 
# 
#  请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种
#  顺序即可。 
# 
#  字符串 s 字典顺序小于 字符串 t 有两种情况： 
# 
#  
#  在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。 
#  如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：words = ["wrt","wrf","er","ett","rftt"]
# 输出："wertf"
#  
# 
#  示例 2： 
# 
#  
# 输入：words = ["z","x"]
# 输出："zx"
#  
# 
#  示例 3： 
# 
#  
# 输入：words = ["z","x","z"]
# 输出：""
# 解释：不存在合法字母顺序，因此返回 "" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 100 
#  1 <= words[i].length <= 100 
#  words[i] 仅由小写英文字母组成 
#  
# 
#  
# 
#  
#  注意：本题与主站 269 题相同： https://leetcode-cn.com/problems/alien-dictionary/ 
# 
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 数组 字符串 👍 129 👎 0
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 建图,确定入度
        graph = dict()
        inDegrees = dict()
        for word in words:
            for ch in word:
                if ch not in graph:
                    graph[ch] = set()
                if ch not in inDegrees:
                    inDegrees[ch] = 0
        # 相邻单词之间两两比较:
        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            if w1.startswith(w2) and w1!=w2:
                return ""
            j = 0
            while j < len(w1) and j < len(w2):
                ch1 = w1[j]
                ch2 = w2[j]
                if ch1 != ch2:
                    if ch2 not in graph[ch1]:
                        graph[ch1].add(ch2)
                        inDegrees[ch2] +=1

                    break
                j+=1

        # 开始进行拓扑排序，每次选择度为0的节点加入到队列中，同时删掉度为0的节点对应的边（与其连接的节点度减1）
        queue = collections.deque()
        for ch in inDegrees:
            if inDegrees[ch] == 0:
                queue.append(ch)
        res = []
        while queue:
            ch = queue.popleft()
            res.append(ch)
            for nxt in graph[ch]:
                inDegrees[nxt] -= 1
                if inDegrees[nxt] == 0:
                    queue.append(nxt)

        return "".join(res) if len(res) == len(graph) else ""




# leetcode submit region end(Prohibit modification and deletion)
