#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30204
#
# [1] 两数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        方法一：哈希表法（最优解）
        - 思路：
          遍历数组的同时，在哈希表中查找是否存在 target - n（目标补数）。
          若存在，则直接返回其对应下标与当前下标；
          若不存在，则将当前元素与其下标存入哈希表。
        - 时间复杂度: O(n) —— 只需单次遍历，哈希表平均查找/存取为 O(1)
        - 空间复杂度: O(n) —— 最多存储 n 个键值对
        """
        hashmap = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[n] = i
        return []

    # ================= 备选解法（供复习参考） =================
    # 方法二：暴力枚举
    # - 思路：双重循环遍历所有数对，内层循环从 i+1 开始避免重复使用同一元素
    # - 时间复杂度: O(n^2)
    # - 空间复杂度: O(1)
    #
    # def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
    #     n = len(nums)
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    #     return []
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

