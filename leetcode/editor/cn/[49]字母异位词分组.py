# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。 
# 
#  字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]] 
# 
#  示例 2: 
# 
#  
# 输入: strs = [""]
# 输出: [[""]]
#  
# 
#  示例 3: 
# 
#  
# 输入: strs = ["a"]
# 输出: [["a"]] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= strs.length <= 10⁴ 
#  0 <= strs[i].length <= 100 
#  strs[i] 仅包含小写字母 
#  
# 
#  Related Topics 数组 哈希表 字符串 排序 👍 1247 👎 0
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())

        # if not strs:
        #     return []
        # anagrams_dict = dict()
        # for s in strs:
        #     # 这个地方要思考一下，为何要转换成tuple作为key？因为list不能作为key。
        #     # 排序后返回的是一个排序后的字符列表。
        #     # key = tuple(sorted(s))
        #     key = "".join(sorted(s))
        #     anagrams_dict[key] = anagrams_dict.get(key, []) + [s]
        # return list(anagrams_dict.values())

# leetcode submit region end(Prohibit modification and deletion)
