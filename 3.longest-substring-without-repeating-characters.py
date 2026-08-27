#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        方法一：滑动窗口 + 哈希表记录下标（最优解 - 跳跃式更新）
        - 思路：
          1. 使用哈希表 map 记录每个字符最后一次出现的索引下标。
          2. 用 left 和 right 维护滑动窗口的两端。
          3. 遍历到字符 val 时：
             若 val 已在哈希表中，左边界 left 一步跳跃到 max(map[val] + 1, left)，
             使用 max 是为了防止 left 倒退回历史窗口之外的位置（例如针对 "abba" 用例）。
          4. 更新字符 val 的最新下标，并计算当前窗口长度更新最大值 res。
        
        复杂度分析：
        - 时间复杂度: O(n) —— 仅需单次遍历，右指针扩展，左指针一步跳跃，每个字符只访问 1 次
        - 空间复杂度: O(|Σ|) —— 哈希表最多存储字符集大小个键值对（ASCII 字符集上限为 128）
        """
        map = {}
        left = 0
        res = 0
        for right, val in enumerate(s):
            if val in map:
                left = max(map[val] + 1, left)
            map[val] = right
            res = max(res, right - left + 1)
        return res

    # ================= 备选解法（供复习参考） =================
    # 方法二：经典滑动窗口 + Set 集合（逐位收缩法）
    # - 思路：
    #   1. 右指针不断将新字符加入 set 集合。
    #   2. 当遇到已存在的重复字符时，左指针通过 while 循环逐步收缩，
    #      并依次从 set 中移除字符，直到窗口内无重复字符。
    # - 时间复杂度: O(n) —— 每个字符最多进入和移出窗口各 1 次，共 2n 次操作
    # - 空间复杂度: O(|Σ|) —— 集合中最多存储当前无重复窗口内的字符
    #
    # def lengthOfLongestSubstring_set(self, s: str) -> int:
    #     seen = set()
    #     left = 0
    #     res = 0
    #     for right, val in enumerate(s):
    #         while val in seen:
    #             seen.remove(s[left])
    #             left += 1
    #         seen.add(val)
    #         res = max(res, right - left + 1)
    #     return res
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

