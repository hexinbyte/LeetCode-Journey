#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30204
#
# [121] 买卖股票的最佳时机
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        一次遍历贪心/动态规划：维护历史最低买入价格，遍历每天尝试卖出并更新最大利润。
        - 时间复杂度: O(n) —— 仅需单次线性扫描价格数组
        - 空间复杂度: O(1) —— 仅使用常数个变量记录最低价与最大利润
        """
        ans = 0
        left_min = float("inf")
        for price in prices:
            if price > left_min:
                ans = max(ans, price - left_min)
            if price < left_min:
                left_min = price
        return ans


# @lc code=end


#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#
