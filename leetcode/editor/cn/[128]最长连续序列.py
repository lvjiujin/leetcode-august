# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。 
# 
#  请你设计并实现时间复杂度为 O(n) 的算法解决此问题。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics 并查集 数组 哈希表 👍 1414 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    class DisjointSetUnion:

        def __init__(self, nums):
            self.f = dict()
            self.rank = dict()
            # 记录联通分量的节点个数
            self.count = dict()
            for num in nums:
                self.f[num] = num
                self.rank[num] = 1
                self.count[num] = 1

        def find(self, x: int):
            if x not in self.f:
                return None
            if self.f[x] != x:
                self.f[x] = self.find(self.f[x])

            return self.f[x]

        def unionSet(self, x: int, y: int):
            fx, fy = self.find(x), self.find(y)
            if fx == fy:
                return self.count[fx]
            if self.rank[fx] < self.rank[fy]:
                fx, fy = fy, fx
            self.rank[fx] += self.rank[fy]
            self.f[fx] = fy
            self.count[fy] += self.count[fx]

            return self.count[fy]

        def numberOfConnectedComponent(self) -> int:
            total = sum(1 for x, fa in self.f.items() if x == fa)

            return total

    def longestConsecutive(self, nums: List[int]) -> int:
        # 字节跳动原题，要引起足够的重视。

        if not nums:
            return 0
        dsu = Solution.DisjointSetUnion(nums)
        ans = 1
        for num in nums:
            # 注意，这个地方不能写成 if dsu.find(num + 1) 因为find的返回值可能为0.
            if dsu.find(num + 1) is not None:
                ans = max(ans, dsu.unionSet(num, num + 1))
        return ans
    # 方法二：哈希集合
    def longestConsecutive(self, nums: List[int]) -> int:
        # 建立一个存储所有数的哈希表，同时起到去重功能
        hash_set = set()
        for num in nums:
            hash_set.add(num)
        ans = 0
        # 遍历去重后的所有数字
        for num in hash_set:
            cur = num
        # 只有当num-1不存在时，才开始向后遍历num+1，num+2，num+3......
            if (cur - 1) not in hash_set:
                while (cur+1) in hash_set:
                    cur += 1
            # [num, cur]之间是连续的，数字有cur - num + 1个
            ans = max(ans, cur - num + 1)

        return ans

    # 方法三：哈希+右边界
    def longestConsecutive(self, nums: List[int]) -> int:

        #  key表示num，value表示num最远到达的连续右边界
        map = dict()
        # 初始化每个num的右边界为自己
        for num in nums:
            map[num] = num
        ans = 0
        for num in nums:
            if (num - 1) not in map:
                right = map[num]
                # 遍历得到最远的右边界
                while (right + 1) in map:
                    right = map[right + 1]
                # 更新右边界
                map[num] = right
                ans = max(ans, right - num + 1)
        return ans

    # 方法三：哈希表记录连续区间长度（动态规划）
    def longestConsecutive(self, nums: List[int]) -> int:

        # key表示num，value表示num所在连续区间的长度
        map = dict()
        ans = 0
        for num in nums:
            # 当map中不包含num，也就是num第一次出现
            if num not in map:
                # left为num-1所在连续区间的长度，更进一步理解为：左连续区间的长度
                left = map.get(num - 1, 0)
                # right为num+1所在连续区间的长度，更进一步理解为：右连续区间的长度
                right = map.get(num + 1, 0)
                # 当前连续区间的总长度
                curLen = left + right + 1
                ans = max(ans, curLen)
                # 将num加入map中，表示已经遍历过该值。其对应的value可以为任意值。
                map[num] = -1
                # 更新当前连续区间左边界和右边界对应的区间长度
                map[num - left] = curLen
                map[num + right] = curLen

        return ans

# leetcode submit region end(Prohibit modification and deletion)
