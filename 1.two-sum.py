#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30204
#
# [1] 两数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 使用哈希表解法，时间复杂度O(n)，空间复杂度O(n)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap  = {}
#         for i,n in enumerate(nums):
#             comple = target - n
#             if comple in map:
#                 return [map[comple], i]
#             map[n] = i


# 暴力解法，时间复杂度O(n^2)，空间复杂度O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v1 in enumerate(nums):
            for j in range(i+1, len(nums)):
                v2 = nums[j]
                if v1 + v2 == target:
                    return [i,j]
                
        
        
# @lc code=end


#
# @lcpr case=start
# [2,7,11,15]\n18\n
# @lcpr case=end

#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

