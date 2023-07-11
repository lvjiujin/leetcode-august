# 给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，并且这两个单词不含有公共字母
# 。如果不存在这样的两个单词，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出：16 
# 解释：这两个单词为 "abcw", "xtfn"。 
# 
#  示例 2： 
# 
#  
# 输入：words = ["a","ab","abc","d","cd","bcd","abcd"]
# 输出：4 
# 解释：这两个单词为 "ab", "cd"。 
# 
#  示例 3： 
# 
#  
# 输入：words = ["a","aa","aaa","aaaa"]
# 输出：0 
# 解释：不存在这样的两个单词。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= words.length <= 1000 
#  1 <= words[i].length <= 1000 
#  words[i] 仅包含小写字母 
#  
# 
#  Related Topics 位运算 数组 字符串 👍 381 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = defaultdict(int)
        for word in words:
            print("word = ", word)
            mask = reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0)
            print("mask = {} ---------".format(mask))
            masks[mask] = max(masks[mask], len(word))
        return max((masks[x] * masks[y] for x, y in product(masks, repeat=2) if x & y == 0), default=0)

        # if not words:
        #     return 0
        # length = len(words)
        # flags = [[False for _ in range(26)] for _ in range(length)]
        # res = 0
        # for i in range(length):
        #     for c in words[i]:
        #         flags[i][ord(c) - ord('a')] = True
        #
        # for i in range(length - 1):
        #     for j in range(i + 1, length):
        #         k = 0
        #         for k in range(26):
        #             if words[i][k] and words[j][k]:
        #                 break
        #         if k == 26:
        #             prob = len(words[i]) * len(words[j])
        #             print("prob = ", prob)
        #             res = max(res, prob)
        # return res
        # python中的reduce和product函数的学习复习温习。

# leetcode submit region end(Prohibit modification and deletion)
