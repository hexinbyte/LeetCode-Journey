#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30204
#
# [70] 爬楼梯
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        利用动态规划（滚动数组）状态压缩求解斐波那契数列。
        到达第 n 阶的方法数等于到达第 n-1 阶与第 n-2 阶方法数之和，常数变量滚动推导即可。
        - 时间复杂度: O(n) —— 仅需单重循环迭代 n 次
        - 空间复杂度: O(1) —— 仅使用常数个滚动变量存储前两项状态
        """
        # 距离step低2阶和1阶的可能性,初始化step为3
        ans_2 = 1
        ans_1 = 2
        for _ in range(3,n):
            ans_1,ans_2 = ans_1 + ans_2,ans_1
        return ans_2 if n == 1 else (ans_1 if n == 2 else ans_1 + ans_2)


# @lc code=end


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#
