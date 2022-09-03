# Given an array of strings strs, group the anagrams together. You can return 
# the answer in any order. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#  
#  Example 2: 
#  Input: strs = [""]
# Output: [[""]]
#  
#  Example 3: 
#  Input: strs = ["a"]
# Output: [["a"]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 10⁴ 
#  0 <= strs[i].length <= 100 
#  strs[i] consists of lowercase English letters. 
#  
# 
#  Related Topics Array Hash Table String Sorting 👍 11376 👎 360


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = dict()
        for s in strs:
            key = tuple(sorted(s))
            anagrams_dict[key] = anagrams_dict.get(key, []) + [s]

        return list(anagrams_dict.values())


        
# leetcode submit region end(Prohibit modification and deletion)
