# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  
# 
#  注意： 
# 
#  
#  对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。 
#  如果 s 中存在这样的子串，我们保证它是唯一的答案。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 10⁵ 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 进阶：你能设计一个在 
# o(n) 时间内解决此问题的算法吗？
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 2187 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        import collections
        charToCount = collections.defaultdict(int)
        # 首先统计字符串t中字符的词频，放到字典 charToCount中。
        # 注意charToCount始终记录当前滑动窗口下，我们还需要的元素数量。
        for ch in t:
            charToCount[ch] += 1
        # count 表示我们需要的非重复字符个数。
        count = len(charToCount)
        start, end, minStart, minEnd = [0, 0, 0, 0]
        shortest = 10 ** 5 + 1  # 字符串最大长度为10**5,所以这里这样初始化。
        while end < len(s) or (count == 0 and end == len(s)):
            # count == 0说明start-end两个指针之间的子字符串已经包含了字符串t中的所有字符。
            # end == len(s) 说明已经达到s字符串末尾。此时需要检查start。
            if count > 0:
                endCh = s[end]
                # endCh在charToCount中，说明end指针指向的元素是我们需要的，因此charToCount中该元素数量-1。
                if endCh in charToCount:
                    charToCount[endCh] -= 1
                    # 如果该元素数量为0，说明，我们不需要该元素了（已经遇见过了），所以需要的不同字符个数count -1.
                    if charToCount[endCh] == 0:
                        count -= 1
                # 只要count不为0,说明start-end之间的子串没有包含t中的所有字符，所以end继续右移。
                end += 1
            else:
                # 此时：start - end之间的子字符串包含了t中的所有字符。
                # 所以需要记录下此时的shortest.和minStart, minEnd.
                if end - start < shortest:
                    shortest = end - start
                    minStart = start
                    minEnd = end
                startCh = s[start]
                # 如果start指向的元素在charToCount，说明该元素是必须包含的
                # 记住：charToCount记录了当前滑动窗口下我们还需要的元素个数。
                # (但是实际上包含不了了，因为start指针要右移)，故该元素的数量要加1.
                if startCh in charToCount:
                    charToCount[startCh] += 1
                    if charToCount[startCh] == 1:  # ==1 说明，刚好加进来，需要该元素，故需要的元素数量 count +1.
                        count += 1

                start += 1  # start 指针右移。

        return s[minStart:minEnd] if shortest < (10 ** 5 + 1) else ""

        # 方法二：
        # import collections
        # need = collections.defaultdict(int)
        # for c in t:
        #     need[c] += 1
        # needCnt = len(t)
        # i = 0
        # res = (0, float('inf'))
        # for j, c in enumerate(s):
        #     if need[c] > 0:
        #         needCnt -= 1
        #     need[c] -= 1
        #     if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
        #         while True:  # 步骤二：增加i，排除多余元素
        #             c = s[i]
        #             if need[c] == 0:
        #                 break
        #             need[c] += 1
        #             i += 1
        #         if j - i < res[1] - res[0]:  # 记录结果
        #             res = (i, j)
        #         need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
        #         needCnt += 1
        #         i += 1
        # return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果




# leetcode submit region end(Prohibit modification and deletion)
