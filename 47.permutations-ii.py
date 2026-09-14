#
# @lc app=leetcode.cn id=47 lang=python3
# @lcpr version=30204
#
# [47] 全排列 II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        先排序使相同数字相邻，利用 used 数组记录使用状态进行回溯。
        当遇到相同数字且前一个数字已回溯释放（树层重复）时进行剪枝去重。
        - 时间复杂度: O(n * n!) —— 最坏全不重复时递归探索全部排列并拷贝
        - 空间复杂度: O(n) —— 递归栈深度为 n，used 与 path 数组占用 O(n) 空间
        """
        nums.sort()
        n = len(nums)
        ans = []
        path = []
        used = [False] * n
        def backtrack():
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                # 如果这个数字当前分支已经在用了，跳过
                if used[i]:
                    continue
                # 🌟 核心灵魂剪枝代码：
                # 如果当前数字和前一个数字相同，且前一个数字刚被回溯释放（not used[i-1]）
                # 说明在当前这个位置上，之前已经选过这个相同的数字了，直接跳过！
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                # 做选择
                used[i] = True
                path.append(nums[i])
                # 递归
                backtrack()
                # 撤销选择（回溯）
                path.pop()
                used[i] = False
        backtrack()
        return ans

    # ------------------ 备选解法（原地交换 + 局部哈希集合去重） ------------------
    # 原地交换元素构建排列，每层递归固定当前 first 位置时，用局部 visited 保证同个数值只被换过去一次。
    # - 时间复杂度: O(n * n!) —— 探索全部合法排列并拷贝
    # - 空间复杂度: O(n^2) —— 递归栈深度为 n，最深调用栈上同时存活的局部 set 占用 O(n^2) 空间
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    #     ans = []
    #     n = len(nums)

    #     def dfs(first: int):
    #         if first == n:
    #             ans.append(nums[:])
    #             return

    #         visited = set()
    #         for i in range(first, n):
    #             if nums[i] in visited:
    #                 continue
    #             visited.add(nums[i])

    #             nums[first], nums[i] = nums[i], nums[first]

    #             dfs(first + 1)

    #             nums[first], nums[i] = nums[i], nums[first]

    #     dfs(0)
    #     return ans

# @lc code=end


#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#
