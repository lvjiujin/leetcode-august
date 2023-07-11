# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
# 
#  给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组 [3
# ,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。 
# 
#  注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], 
# ..., a[n-2]] 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：numbers = [3,4,5,1,2]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：numbers = [2,2,2,0,1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == numbers.length 
#  1 <= n <= 5000 
#  -5000 <= numbers[i] <= 5000 
#  numbers 原来是一个升序排序的数组，并进行了 1 至 n 次旋转 
#  
# 
#  注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-
# sorted-array-ii/ 
# 
#  Related Topics 数组 二分查找 👍 721 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minArray1(self, numbers: List[int]) -> int:
        # 二分法的思想: 注意边界问题。
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = left + (right - left) //2
            if numbers[mid] < numbers[right]:
                # 中间小于最右边，说明最小值肯定在左半部分。mid可能是最小值，所以用等号。
                right = mid
            elif numbers[mid] > numbers[right]:
                # 中间大于最右边，说明最小值在右半部分 ,mid不可能是最小值，所以mid + 1
                left = mid + 1
            else:
                right -= 1
        return numbers[left]

    def minArray2(self, numbers: List[int]) -> int:
        import heapq
        heapq.heapify(numbers)
        return heapq.heappop(numbers)

    def minArray(self, numbers: List[int]) -> int:
        # 方法一：
        min_value = numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i-1]:
                if i + 1 < len(numbers) and numbers[i] < numbers[i+1]:
                    return numbers[i]
                if numbers[i] < min_value:
                    min_value = numbers[i]

        return min_value





# leetcode submit region end(Prohibit modification and deletion)
