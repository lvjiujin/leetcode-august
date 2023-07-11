# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。 
# 
#  算法的时间复杂度应该为 O(log (m+n)) 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -10⁶ <= nums1[i], nums2[i] <= 10⁶ 
#  
# 
#  Related Topics 数组 二分查找 分治 👍 6093 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0  # index1和index2作为起始点，相当于两个数组变化的start。
            while True:
                # 特殊情况
                if index1 == m:     # nums1 到达数组末尾了,nums1将为空，只要选择nums2从index2开始的第k个元素。
                    return nums2[index2 + k - 1]
                if index2 == n:    # nums2 到达数组末尾了，nums2将为空,只要选择nums1从index1开始的第k个元素即可。
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况 ， newIndex1，newIndex2为参与比较的点，pivot1和pivot2的下标。
                newIndex1 = min(index1 + k // 2 - 1, m - 1)  # 防止越界
                newIndex2 = min(index2 + k // 2 - 1, n - 1)  # 防止越界
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1  # k=k−k/2  end - start + 1才是真正的要减去的长度。
                    index1 = newIndex1 + 1  # index1从结束位置(比较位置，newIndex1)向后移动一位.
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1  # 新的开始位置从原来的结束位置向后移动一位，即index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2



# leetcode submit region end(Prohibit modification and deletion)
