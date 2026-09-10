#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        方法一：贪心算法 / 动态规划（Kadane 算法，最优解）
        - 思路：
          1. 遍历数组，t_max 维护当前连续子数组的和。
          2. 实时用 t_max 更新全局最大值 ans。
          3. 若 t_max < 0，说明当前连续和为负贡献，果断重置为 0，从下一元素重新起跑。
        - 复杂度：
          - 时间复杂度: O(n) —— 仅遍历一遍数组
          - 空间复杂度: O(1) —— 常数额外空间
        """
        ans = nums[0]
        t_max = 0
        for num in nums:
            t_max += num
            if t_max > ans:
                ans = t_max
            if t_max < 0:
                t_max = 0
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

