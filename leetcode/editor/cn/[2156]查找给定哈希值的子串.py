# 给定整数 p 和 m ，一个长度为 k 且下标从 0 开始的字符串 s 的哈希值按照如下函数计算： 
# 
#  
#  hash(s, p, m) = (val(s[0]) * p⁰ + val(s[1]) * p¹ + ... + val(s[k-1]) * pᵏ⁻¹) 
# mod m. 
#  
# 
#  其中 val(s[i]) 表示 s[i] 在字母表中的下标，从 val('a') = 1 到 val('z') = 26 。 
# 
#  给你一个字符串 s 和整数 power，modulo，k 和 hashValue 。请你返回 s 中 第一个 长度为 k 的 子串 sub ，满足 
# hash(sub, power, modulo) == hashValue 。 
# 
#  测试数据保证一定 存在 至少一个这样的子串。 
# 
#  子串 定义为一个字符串中连续非空字符组成的序列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0
# 输出："ee"
# 解释："ee" 的哈希值为 hash("ee", 7, 20) = (5 * 1 + 5 * 7) mod 20 = 40 mod 20 = 0 。
# "ee" 是长度为 2 的第一个哈希值为 0 的子串，所以我们返回 "ee" 。
#  
# 
#  示例 2： 
# 
#  输入：s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32
# 输出："fbx"
# 解释："fbx" 的哈希值为 hash("fbx", 31, 100) = (6 * 1 + 2 * 31 + 24 * 31²) mod 100 = 23
# 132 mod 100 = 32 。
# "bxz" 的哈希值为 hash("bxz", 31, 100) = (2 * 1 + 24 * 31 + 26 * 31²) mod 100 = 2573
# 2 mod 100 = 32 。
# "fbx" 是长度为 3 的第一个哈希值为 32 的子串，所以我们返回 "fbx" 。
# 注意，"bxz" 的哈希值也为 32 ，但是它在字符串中比 "fbx" 更晚出现。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= s.length <= 2 * 10⁴ 
#  1 <= power, modulo <= 10⁹ 
#  0 <= hashValue < modulo 
#  s 只包含小写英文字母。 
#  测试数据保证一定 存在 满足条件的子串。 
#  
# 
#  Related Topics 字符串 滑动窗口 哈希函数 滚动哈希 👍 37 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import string


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:

        mult = 1  # power^k mod modulo
        n = len(s)
        pos = -1  # 第一个符合要求子串的起始下标
        h = 0  # 子串哈希值
        # 预处理计算最后一个子串的哈希值和 power^k mod modulo
        # 第一个for 循环是计算出最末k个字符的子串的hash值。它是后续滑动窗口的基础。
        for i in range(n - 1, n - k - 1, -1):
            h = (h * power + (ord(s[i]) - 96)) % modulo
            if i != n - k:
                mult = mult * power % modulo
        if h == hashValue:
            pos = n - k
        # 向前计算哈希值并尝试更新下标
        for i in range(n - k - 1, -1, -1):
            h = ((h - (ord(s[i + k]) - 96) * mult % modulo + modulo) * power + (
                        ord(s[i]) - 96)) % modulo
            if h == hashValue:
                pos = i
        return s[pos:pos + k]


        # alpha = string.ascii_lowercase
        # digit = [i for i in range(1,27)]
        # alpha_dict = dict(zip(alpha, digit))
        # sl = len(s)
        # if k >=sl:
        #     sub_digit = [int(alpha_dict[x]) for x in s]
        #     hash_value = 0
        #     for i, x in enumerate(sub_digit):
        #         hash_value += x * (power ** i)
        #     hash_value %= modulo
        #     if hash_value == hashValue:
        #         return s
        # else:
        #     for i in range(sl-k):
        #         sub = s[i:i+k]
        #         sub_digit = [int(alpha_dict[x]) for x in sub]
        #         hash_value = 0
        #         for i, x in enumerate(sub_digit):
        #             hash_value += x* (power ** i)
        #         hash_value %= modulo
        #         if hash_value == hashValue:
        #             return sub





# leetcode submit region end(Prohibit modification and deletion)
