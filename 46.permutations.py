#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30204
#
# [46] 全排列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        方法一：函数式回溯 / 集合差集递归（简洁免疫 Bug）
        - 思路：
          1. t_nums 记录当前路径，nums_set 维护当前剩余可用数字集合。
          2. 终止条件：nums_set 为空时说明全部排列完毕，收集结果。
          3. 分支推进：利用 t_nums + [num] 与 nums_set - {num} 产生全新对象，天生无需手动撤销选择。
        - 复杂度：
          - 时间复杂度: O(n * n!) —— 全排列总数为 n!，生成每个排列耗时 O(n)
          - 空间复杂度: O(n * n!) —— 递归过程中不断产生新的 list 与 set 对象
        """
        def dfs(t_nums, nums_set):
            if not nums_set:
                ans.append(t_nums)
                return
            for num in nums_set:
                dfs(t_nums + [num], nums_set - {num})

        ans = []
        nums_set = set(nums)
        dfs([], nums_set)
        return ans

    # ================= 备选解法（供复习参考） =================
    # 方法二：原地交换法（In-place Swap，空间 O(1) 最优解）
    # - 思路：first 指针表示当前待确定的位置，从 [first, n-1] 中选数字与 first 交换，递归决定下一位，返回后再交换恢复现场。
    # - 时间复杂度: O(n * n!)
    # - 空间复杂度: O(1) —— 除结果集与递归栈外无任何额外辅助空间
    #
    #     ans = []
    #     n = len(nums)

    #     def dfs(first: int):
    #         if first == n:
    #             ans.append(nums[:])
    #             return
    #         for i in range(first, n):
    #             nums[first], nums[i] = nums[i], nums[first]

    #             dfs(first + 1)

    #             nums[first], nums[i] = nums[i], nums[first]

    #     dfs(0)
    #     return ans


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
