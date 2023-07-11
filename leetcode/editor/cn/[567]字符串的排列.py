# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。 
# 
#  换句话说，s1 的排列之一是 s2 的 子串 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#  
# 
#  示例 2： 
# 
#  
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s1.length, s2.length <= 10⁴ 
#  s1 和 s2 仅包含小写字母 
#  
# 
#  Related Topics 哈希表 双指针 字符串 滑动窗口 👍 773 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        cnt1 = [0 for _ in range(26)]
        cnt2 = [0 for _ in range(26)]

        for i in range(m):
            cnt1[ord(s1[i]) - ord('a')] += 1
            cnt2[ord(s2[i]) - ord('a')] += 1

        if cnt1 == cnt2:
            return True
        left = 0
        for right in range(m, n):
            cnt2[ord(s2[left]) - ord('a')] -= 1
            cnt2[ord(s2[right]) - ord('a')] += 1
            left += 1
            if cnt1 == cnt2:
                return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
