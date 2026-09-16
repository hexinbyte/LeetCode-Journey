#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        利用滑动窗口与双哈希表维护字符频次，通过 valid 计数器判断窗口是否完全覆盖 t。
        右指针扩展窗口寻求解，满足条件时收缩左指针更新最小覆盖子串的起始位置与长度。
        - 时间复杂度: O(|s| + |t|) —— 统计 t 耗时 O(|t|)，左右指针各遍历 s 最多一次
        - 空间复杂度: O(|Σ|) —— 字符集大小，哈希表最多存储常数个 ASCII 字符
        """
        need = Counter(t)
        #默认值为0的字典
        window = defaultdict(int)

        # 记录达标字符数
        valid = 0
        left = 0
        start = 0
        min_len = float('inf')

        for right, char in enumerate(s):
            if char in need:
                window[char] += 1
                if need[char] == window[char]:
                    valid += 1

                while valid == len(need):
                    if right - left + 1 < min_len:
                        min_len = right - left + 1
                        start = left
                    left_char = s[left]
                    if left_char in need:
                        if window[left_char] == need[left_char]:
                            valid -= 1
                        window[left_char] -= 1
                    left += 1

        return "" if min_len == float('inf') else s[start: start+min_len]


# @lc code=end


#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#
