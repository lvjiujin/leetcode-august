# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,5,6,4]
# 输出: 5 
# 
#  
# 
#  限制： 
# 
#  0 <= 数组长度 <= 50000 
# 
#  Related Topics 树状数组 线段树 数组 二分查找 分治 有序集合 归并排序 👍 891 👎 0


import copy
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    # 归并排序法:
    def reversePairs(self, nums: List[int]) -> int:
        copyData = copy.copy(nums)
        if not nums or len(nums) < 2: # 边界情况一定要考虑
            return 0

        def reversePairsCore(data, copyData, start, end):
            if start == end:
                copyData[start] = data[start]
                return 0
            size = (end - start) // 2
            left = reversePairsCore(copyData, data, start, start + size)
            right = reversePairsCore(copyData, data, start + size + 1, end)
            # i 初始化为前半段最后一个数字的下标
            i = start + size
            # j 初始化为后半段最后一个数字的下标
            j = end
            indexCopy = end
            count = 0
            while i >= start and j >= start + size + 1:
                if data[i] > data[j]:
                    copyData[indexCopy] = data[i]
                    indexCopy -= 1
                    i -= 1
                    count += j - start - size
                else:
                    copyData[indexCopy] = data[j]
                    indexCopy -= 1
                    j -= 1
            while i >= start:
                copyData[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1

            while j >= start + size + 1:
                copyData[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1
            # print("count = ", count)
            return left + right + count

        res = reversePairsCore(nums, copyData, 0, len(nums) - 1)
        print("nums = ", nums)
        return res



# leetcode submit region end(Prohibit modification and deletion)
