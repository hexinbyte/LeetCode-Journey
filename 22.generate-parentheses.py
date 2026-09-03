#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30204
#
# [22] 括号生成
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        方法一：回溯法 / 深度优先搜索（DFS）
        - 思路：
          1. 通过记录已放置的左括号数 left 与右括号数 right 进行合法性剪枝。
          2. 终止条件：当 right == n 时，说明 n 对括号已全部配对闭合，将当前路径 s 收集到 ans 中。
          3. 分支转移：
             - 若 left == right：当前左右括号平衡，下一个字符只能放左括号 '('。
             - 若 left > right：
               - 若 left < n：仍有左括号配额，可放左括号 '('。
               - 若 right < n：可放右括号 ')' 与已有的左括号配对。
        - 复杂度：
          - 时间复杂度: O(4^n / sqrt(n)) —— 结果数量为第 n 个卡特兰数，每个组合生成耗时 O(n)
          - 空间复杂度: O(n) —— 递归调用栈深度最大为 2n
        """

        def dfs(s: str, left: int, right: int):
            # 终止条件：所有右括号已放满，当前字符串构建完成
            if right == n:
                ans.append(s)
            elif left == right:
                # 左右相等时只能放左括号
                dfs(s + "(", left + 1, right)
            else:
                # 还有左括号配额时可放左括号
                if left < n:
                    dfs(s + "(", left + 1, right)
                # 可放右括号进行匹配
                if right < n:
                    dfs(s + ")", left, right + 1)

        ans = []
        dfs("", 0, 0)
        return ans


# @lc code=end


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
