# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 
#  
# 输入：nums = [3,10,5,25,2,8]
# 输出：28
# 解释：最大运算结果是 5 XOR 25 = 28. 
# 
#  示例 2： 
# 
#  
# 输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# 输出：127
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁵ 
#  0 <= nums[i] <= 2³¹ - 1 
#  
# 
#  Related Topics 位运算 字典树 数组 哈希表 👍 492 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

class Trie:
    def __init__(self):
        self.child = [None for _ in range(2)]

    def insert(self, x: int) -> None:
        root = self
        for i in range(31, -1, -1):
            ID = (x >> i) & 1
            if root.child[ID] is None:
                root.child[ID] = Trie()
            root = root.child[ID]

    def query(self, x: int) -> int:
        root = self
        res = 0
        for i in range(31, -1, -1):
            ID = (x >> i) & 1
            if root.child[1 - ID] is not None:
                res = res * 2 + 1
                # print('xor = ', res)
                root = root.child[1 - ID]
            else:
                res = res * 2
                # print('xor = ', res)
                root = root.child[ID]

        return res


class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(2)]


class Solution:


    def findMaximumXOR2(self, nums: List[int]) -> int:
        n = len(nums)

        T = Trie()
        res = 0
        for x in nums:
            T.insert(x)
            res = max(res, T.query(x))
        return res

    def findMaximumXOR(self, nums: List[int]) -> int:
        class TrieNode:
            def __init__(self):
                self.children = [None for _ in range(2)]

        root = TrieNode()
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                # print("bit = ", bit)
                if node.children[bit] is None:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        max_res = 0
        for num in nums:
            node = root
            xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1

                if node.children[1 - bit] is not None:
                    xor = xor *2 + 1
                    node = node.children[1 - bit]
                else:
                    xor = xor * 2
                    node = node.children[bit]

            max_res = max(max_res, xor)
        return max_res

# leetcode submit region end(Prohibit modification and deletion)
