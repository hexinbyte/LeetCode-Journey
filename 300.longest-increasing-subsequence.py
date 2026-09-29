#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=30204
#
# [300] 最长递增子序列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        动态规划解法。
        定义 dp[i] 为以 nums[i] 结尾的最长递增子序列长度，遍历前面所有 j < i 状态转移：dp[i] = max(dp[i], dp[j] + 1)。
        - 时间复杂度: O(n^2) —— 双重循环遍历所有状态与转移
        - 空间复杂度: O(n) —— 长度为 n 的一维 dp 数组
        """
        dp = [1 for _ in range(len(nums))]
        max_dp = 0
        for i, num in enumerate(nums):
            for j in range(0, i):
                if num > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
            max_dp = max(max_dp, dp[i])
        return max_dp


# @lc code=end


#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#
