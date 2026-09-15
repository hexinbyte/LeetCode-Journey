#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30204
#
# [209] 长度最小的子数组
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        利用滑动窗口（双指针）维护连续子数组和。
        右指针扩展窗口累加求和，当和达到 target 时不断收缩左指针更新最小长度。
        - 时间复杂度: O(n) —— 左右指针各自最多遍历数组一次
        - 空间复杂度: O(1) —— 仅使用常数级额外变量
        """
        if not nums:
            return 0
        slow, fast = 0, 0
        window_sum = 0
        ans = float('inf')
        while fast < len(nums):
            window_sum += nums[fast]
                
            while window_sum >= target:
                ans = min(ans, fast - slow + 1)
                window_sum -= nums[slow]
                slow += 1

            fast += 1
        return 0 if ans == float('inf') else ans


# @lc code=end


#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#
