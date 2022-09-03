# 给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
# 解释：[4,9] 也是可通过的
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums1.length, nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 1000 
#  
#  Related Topics 数组 哈希表 双指针 二分查找 排序 👍 544 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        # return list(set(nums1).intersection(set(nums2)))
        # return list(set(nums1) & set(nums2)) # &符号在这里表示求交集。
        s1 = set(nums1)
        s2 = set(nums2)
        l1, l2 = len(s1), len(s2)
        res = []
        if l1 < l2:
            for i in s1:
                if i in s2:
                    res.append(i)
        else:
            for i in s2:
                if i in s1:
                    res.append(i)
        return res

        # s = set()
        # for x in nums1:
        #     if x not in s:
        #         s.add(x)
        # res = set()
        # for y in nums2:
        #     if y in s:
        #         res.add(y)
        #
        # return list(res)

# leetcode submit region end(Prohibit modification and deletion)
