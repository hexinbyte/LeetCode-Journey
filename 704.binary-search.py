#
# @lc app=leetcode.cn id=704 lang=python3
# @lcpr version=30204
#
# [704] 二分查找
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        在有序数组闭区间 [left, right] 内进行二分查找。
        - 时间复杂度: O(log n) —— 每次比对使搜索区间折半
        - 空间复杂度: O(1) —— 仅使用常数级指针变量
        """
        left,right = 0,len(nums)-1
        while left<=right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        
# @lc code=end



#
# @lcpr case=start
# [-1,0,3,5,9,12]\n9\n
# @lcpr case=end

# @lcpr case=start
# [-1,0,3,5,9,12]\n2\n
# @lcpr case=end

#

