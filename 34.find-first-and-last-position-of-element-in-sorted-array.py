#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30204
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        两次二分查找（寻找下界模板）：复用查找首个 >= x 位置的逻辑，分别寻找 target 和 target+1 的下界。
        - 时间复杂度: O(log n) —— 两次独立的二分查找，每次 O(log n)
        - 空间复杂度: O(1) —— 仅使用常数个指针变量
        """
        def firstArrive(num:int):
            left,right=0,len(nums)-1
            while right >= left:
                mid = left + (right - left) // 2
                if nums[mid] >= num:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        l = firstArrive(target)
        if l == len(nums) or nums[l] != target:
            return [-1,-1]

        r = firstArrive(target+1) - 1
        return [l,r]


# @lc code=end


#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#
