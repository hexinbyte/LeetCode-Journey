#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30204
#
# [5] 最长回文子串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        方法一：优化版中心扩散法（连续段折叠 + 步长跳跃 + 提前剪枝，推荐最优解）
        - 思路：
          1. 遍历字符串，先圈出当前字符所有连续相同的段 [left, right] 作为扩散中心。
             - 连续相同字符内部天然是回文，无需重复测试内部子中心。
          2. 以 [left, right] 整个区间为中心向两侧双向扩散，寻找最长回文子串。
          3. 跳跃优化：下一轮搜索直接跳到 left = right + 1，跳过所有重复字符。
          4. 提前剪枝：当剩余待查长度已无法超过当前最长回文的一半时 (n - left <= len(res) // 2)，直接 break 提前结束。
        
        复杂度分析：
        - 时间复杂度: 平均接近 O(n)，最坏 O(n^2) —— 运行常数极小，绝大多数用例远快于常规 DP
        - 空间复杂度: O(1) —— 仅常数个指针变量
        """
        left = 0
        res = s[0:1]
        n = len(s)

        while left < n:
            # 💡 提前剪枝：剩余长度无法产生更长回文时直接结束
            if n - left <= len(res) // 2:
                break

            # 寻找连续相同字符的右边界（整体作为回文中心）
            right = left
            while right + 1 < n and s[right + 1] == s[left]:
                right += 1
                if right + 1 - left > len(res):
                    res = s[left : right + 1]

            i, j = left, right
            while i - 1 >= 0 and j + 1 < n and s[i - 1] == s[j + 1]:
                i -= 1
                j += 1
                if j + 1 - i > len(res):
                    res = s[i : j + 1]

            # 💡 步长跳跃：直接跳过已处理的重复字符
            left = right + 1
            
        return res

    # ================= 备选解法（供复习参考） =================
    # 方法二：动态规划法（DP 状态转移）
    # - 思路：
    #   1. 定义状态: dp[i][j] 表示子串 s[i..j] 是否为回文串。
    #   2. 状态转移: dp[i][j] = (s[i] == s[j]) and (length <= 3 or dp[i+1][j-1])。
    #   3. 按子串长度由短到长 (length: 2 -> n) 依次填表。
    # - 时间复杂度: O(n^2)
    # - 空间复杂度: O(n^2)
    #
    # def longestPalindrome_dp(self, s: str) -> str:
    #     n = len(s)
    #     dp = [[False] * n for _ in range(n)]
    #     for i in range(n):
    #         dp[i][i] = True
    #
    #     start, max_len = 0, 1
    #     for length in range(2, n + 1):
    #         for i in range(n - length + 1):
    #             j = i + length - 1
    #             if s[i] == s[j]:
    #                 if length <= 3:
    #                     dp[i][j] = True
    #                 else:
    #                     dp[i][j] = dp[i + 1][j - 1]
    #
    #             if dp[i][j] and length > max_len:
    #                 max_len = length
    #                 start = i
    #
    #     return s[start : start + max_len]
# @lc code=end


#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#
