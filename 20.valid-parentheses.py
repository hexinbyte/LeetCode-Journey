#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """
        方法一：辅助栈 + 哈希表匹配（最优解）
        - 思路：
          1. 使用哈希表 pairs 建立“右括号 -> 对应的左括号”映射，便于 O(1) 匹配校验。
          2. 遍历字符串：
             - 遇到右括号：若此时栈为空，或栈顶左括号与当前右括号不匹配，返回 False；匹配成功则弹出栈顶。
             - 遇到左括号：压入栈中等待后续右括号匹配。
          3. 最终检查栈是否为空（not stack），若为空说明全部成功闭合。
        - 复杂度：
          - 时间复杂度: O(n) —— 单次遍历字符串，栈的 push/pop 操作均为 O(1)
          - 空间复杂度: O(n) —— 最坏情况下所有字符均为左括号全部入栈，哈希表占用 O(1) 常数空间
        """
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in pairs:
                # 遇到右括号：若栈空或栈顶左括号不匹配，返回 False
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()  # 匹配成功，弹出左括号
            else:
                # 遇到左括号：入栈等待匹配
                stack.append(char)

        # 若栈为空说明全部成对闭合
        return not stack

# @lc code=end


#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

# @lcpr case=start
# "([)]"\n
# @lcpr case=end

#
