# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "rat", t = "car"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s 和 t 仅包含小写字母 
#  
# 
#  
# 
#  进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
# 
#  Related Topics 哈希表 字符串 排序 👍 649 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # from collections import Counter
        # return Counter(s) == Counter(t)
        # 解法一：
        # if not s or not t or len(s) != len(t):
        #     return False
        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # else:
        #     return False
        # 解法二:
        if not s or not t or len(s) != len(t):
            return False
        char_dict = dict()
        for c in s:
            char_dict[c] = char_dict.get(c, 0) + 1

        for c in t:
            if c not in char_dict or char_dict[c] == 0:
                return False
            char_dict[c] -= 1

        return True

        # 方法三
        # if not s or not t or len(s) != len(t):
        #     return False
        # counts = [ 0 for _ in range(26)]
        # for ch in s:
        #     counts[ord(ch) - ord('a')] += 1
        # for ch in t:
        #     if counts[ord(ch) - ord('a')] == 0:
        #         return False
        #     counts[ord(ch) - ord('a')] -= 1
        # return True




# leetcode submit region end(Prohibit modification and deletion)
