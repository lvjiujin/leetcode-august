# Given two integer arrays nums1 and nums2, return an array of their 
# intersection. Each element in the result must appear as many times as it shows in both 
# arrays and you may return the result in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums1.length, nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 1000 
#  
# 
#  
#  Follow up: 
# 
#  
#  What if the given array is already sorted? How would you optimize your 
# algorithm? 
#  What if nums1's size is small compared to nums2's size? Which algorithm is 
# better? 
#  What if elements of nums2 are stored on disk, and the memory is limited such 
# that you cannot load all elements into the memory at once? 
#  
#  Related Topics Array Hash Table Two Pointers Binary Search Sorting 👍 4458 👎
#  705


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # if not nums1 or not nums2:
        #     return []
        # l1, l2 = len(nums1), len(nums2)
        # i, j = 0, 0
        # nums1.sort()
        # nums2.sort()
        # res = []
        # while i < l1 and j < l2:
        #     if nums1[i] == nums2[j]:
        #         res.append(nums1[i])
        #         i+=1
        #         j+=1
        #     elif nums1[i] < nums2[j]:
        #         i+=1
        #     else:
        #         j+=1
        # return res
        # intersection = set(nums1) & set(nums2)
        #
        # res = []
        # for i in intersection:
        #     res += [i] * min(nums1.count(i), nums2.count(i))
        # return res
        # 运用集合方法
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        import collections
        m = collections.Counter()
        for num in nums1:
            m[num] +=1
        intersection = list()
        for num in nums2:
            if (c := m.get(num, 0)) > 0:
                m[num] -=1
                intersection.append(num)
                if m[num] == 0:
                    m.pop(num)
        return intersection






        
# leetcode submit region end(Prohibit modification and deletion)
