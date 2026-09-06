#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
from collections import deque


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        方法一：单调栈（横向切片求水，按行计算）
        - 思路：
          1. 维护单调递减栈 stack，存储柱子下标。
          2. 当当前柱子 h >= 栈顶高度时，说明构成凹槽，弹出栈顶作为“坑底” i。
          3. 若弹出后栈非空，则新栈顶为“左墙”，当前柱子为“右墙”：
             - 凹槽水高: min(h, height[stack[-1]]) - height[i]
             - 凹槽水宽: index - stack[-1] - 1
             - 累加水面积 = 凹槽水高 * 凹槽水宽
          4. 结算完毕后将当前柱子下标入栈，维持单调性。
        - 复杂度：
          - 时间复杂度: O(n) —— 每个柱子下标最多入栈、出栈各一次
          - 空间复杂度: O(n) —— 栈的额外空间开销
        """
        stack = deque()
        ans = 0
        for index, h in enumerate(height):
            # 遇到高于栈顶的柱子，说明形成凹槽，循环弹出坑底计算横向积水
            while stack and h >= height[stack[-1]]:
                i = stack.pop()
                if stack:
                    ans += (min(h, height[stack[-1]]) - height[i]) * (index - stack[-1] - 1)
            stack.append(index)

        return ans

    # ================= 备选解法（供复习参考） =================
    # 方法二：双向扫描法（正向扫 + 栈逆序反向扫，按列计算）
    # - 思路：正向遍历时遇到不低于左侧最高墙的柱子则清空栈结算水；遍历结束后全局最高峰沉在栈底，
    #         利用栈的后进先出（LIFO）特性从右往左弹出，逆向结算右半部分剩余积水。
    # - 时间复杂度: O(n)
    # - 空间复杂度: O(n)
    # def trap(self, height: List[int]) -> int:
    #     stack = deque()
    #     sum = 0
    #     # 从左往右，入栈并处理
    #     l_height = 0
    #     for h in height:
    #         if stack and h >= l_height:
    #             while stack:
    #                 sum += l_height - stack.pop()
    #         stack.append(h)
    #         if h > l_height:
    #             l_height = h
    #     # 从右往左，处理栈内遗留元素
    #     r_height = 0
    #     while stack:
    #         h = stack.pop()
    #         if h < r_height:
    #             sum += r_height - h
    #         else:
    #             r_height = h
    #     return sum


# @lc code=end


#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,1,7,1,1,5,2,7,6]\n
# @lcpr case=end

#
