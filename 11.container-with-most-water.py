#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30204
#
# [11] 盛最多水的容器
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        方法一：对向双指针 + 贪心移动短板（最优解）
        - 思路：
          1. 首尾双指针：left 指向数组起始，right 指向数组末尾，初始拥有最大宽度。
          2. 木桶短板效应：容器的盛水量取决于两端中较矮的板：
             Area = (right - left) * min(height[left], height[right])
          3. 指针移动策略（贪心）：
             - 若移动长板：宽度必定减小，高度受限于短板无法突破，面积必定单调减小或不变；
             - 若移动短板：虽然宽度减小，但有可能遇到更高的板，从而有机会获得更大面积。
             - 因此每一步必须且只需“将较短板的指针向内收缩”。
          4. 进阶常数加速：移动指针时，如果遇到比当前短板更矮或等高的板，面积必然更小，可以直接跳过。
        
        复杂度分析：
        - 时间复杂度: O(n) —— 两个指针最多相向移动 n 步，单次遍历
        - 空间复杂度: O(1) —— 仅需常数个辅助指针变量
        """
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h_left, h_right = height[left], height[right]
            curr_area = (right - left) * min(h_left, h_right)
            if curr_area > max_area:
                max_area = curr_area

            # 谁矮就移动谁，并跳过内部更矮的无效板
            if h_left < h_right:
                while left < right and height[left] <= h_left:
                    left += 1
            else:
                while left < right and height[right] <= h_right:
                    right -= 1

        return max_area

    # ================= 备选解法（供复习参考） =================
    # 方法二：双重循环暴力枚举
    # - 思路：穷举所有左右边界数对，计算每一种可能的水槽面积并取最大值
    # - 时间复杂度: O(n^2) —— 数据规模达 10^5 时会超时 (TLE)
    # - 空间复杂度: O(1)
    #
    # def maxArea_brute_force(self, height: List[int]) -> int:
    #     max_area = 0
    #     n = len(height)
    #     for left in range(n):
    #         right = n - 1
    #         while height[left] > 0 and right - left > max_area // height[left]:
    #             curr_area = (right - left) * min(height[left], height[right])
    #             if curr_area > max_area:
    #                 max_area = curr_area
    #             right -= 1
    #     return max_area
# @lc code=end



#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#

