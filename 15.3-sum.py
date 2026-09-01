#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30204
#
# [15] 三数之和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        方法一：排序 + 对向双指针（推荐掌握，空间最优解）
        - 思路：
          1. 排序：先对原数组升序排序（时间复杂度 O(n log n)），为双指针单调性夹逼和去重奠定基础。
          2. 固定基准数 left_val（下标 left）：
             - 核心剪枝：若 nums[left] > 0，因数组已排序，后续任意两数之和必大于 0，不可能凑成 0，直接 break 退出。
             - 外层去重：若 left > 0 且 nums[left] == nums[left - 1]，说明该数值已作为第一个数穷举过，为避免重复解，直接 continue 跳过。
          3. 对向双指针夹逼：令 mid = left + 1（左边界），right = len(nums) - 1（右边界）：
             - 若 nums[mid] + nums[right] == -left_val：找到一组有效三元组，记录到结果 ans 中；
               随后向内收缩并跳过所有连续重复的 nums[mid] 与 nums[right]，防止产生重复三元组。
             - 若 nums[mid] + nums[right] > -left_val：说明和偏大，right 指针向左收缩。
             - 若 nums[mid] + nums[right] < -left_val：说明和偏小，mid 指针向右收缩。

        复杂度分析：
        - 时间复杂度: O(n^2) —— 排序耗时 O(n log n)，外层循环 n 次，内层双指针最多遍历 n 步，总时间复杂度 O(n^2)
        - 空间复杂度: O(1) —— 仅需常数个辅助指针变量（不计返回值及语言底层排序所需的 O(log n) 栈空间）
        """
        nums.sort()
        ans = []

        for left, left_val in enumerate(nums):
            # 剪枝：若当前基准数大于 0，后续数字全为正数，三数之和不可能为 0
            if left_val > 0:
                break

            # 外层去重：跳过与前一个位置数值相同的基准数（下标必须从 1 开始判断）
            if left > 0 and left_val == nums[left - 1]:
                continue

            res = -left_val
            mid = left + 1
            right = len(nums) - 1

            while right > mid:
                mid_val = nums[mid]
                right_val = nums[right]
                total = mid_val + right_val

                if total == res:
                    ans.append([left_val, mid_val, right_val])
                    # 内层去重：跳过连续相同的 mid，避免产生重复解
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    # 内层去重：跳过连续相同的 right，避免产生重复解
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 移动到下一组互不相同的候选数
                    right -= 1
                    mid += 1
                elif total > res:
                    right -= 1
                else:
                    mid += 1

        return ans

    # ================= 备选解法（供复习参考） =================
    # 方法二：哈希表频次统计 + 唯一元素分类枚举（空间换时间，避免多重指针去重）
    # - 思路：
    #   1. 用哈希表统计各元素频次，提取去重排序后的唯一数组 nums_list。
    #   2. 分类枚举避免重复：
    #      - 3个相同：仅 [0, 0, 0] 满足条件（count >= 3）；
    #      - 2个相同：以 left_val 出现两次，寻找补数 s = -2 * left_val 是否在哈希表中；
    #      - 3个互异：当 left_val < 0 时，使用双指针在 nums_list[left+1:] 中寻找互异配对并根据单调性剪枝。
    # - 时间复杂度: O(U^2) —— U 为去重后的唯一元素个数 (U <= n)
    # - 空间复杂度: O(n) —— 哈希表及去重数组占用辅助空间
    #
    # def threeSum_hashmap(self, nums: list[int]) -> list[list[int]]:
    #     val_map = {}
    #     nums_list = []
    #     res = []
    #
    #     for item in nums:
    #         if item not in val_map:
    #             nums_list.append(item)
    #         val_map[item] = val_map.get(item, 0) + 1
    #
    #     nums_list.sort()
    #     for i, left_val in enumerate(nums_list):
    #         count = val_map[left_val]
    #         # 1. 三个相同：只有 [0, 0, 0] 满足条件
    #         if left_val == 0 and count >= 3:
    #             res.append([0, 0, 0])
    #         # 2. 两个相同：以 left_val 为成对数
    #         if count >= 2:
    #             s = -2 * left_val
    #             if s != left_val and s in val_map:
    #                 res.append([left_val, left_val, s])
    #         # 3. 三个互异数：只需在 left_val < 0 时搜索
    #         if left_val < 0:
    #             right = len(nums_list) - 1
    #             while right > i:
    #                 right_val = nums_list[right]
    #                 s = -left_val - right_val
    #                 if s >= right_val:
    #                     break
    #                 elif left_val < s < right_val and s in val_map:
    #                     res.append([left_val, s, right_val])
    #                 right -= 1
    #     return res


# @lc code=end


#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0]\n
# @lcpr case=end

#
