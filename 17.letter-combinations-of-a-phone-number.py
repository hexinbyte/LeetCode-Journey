#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30204
#
# [17] 电话号码的字母组合
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        方法一：BFS 广度优先搜索 / 队列层序遍历
        - 思路：
          1. 使用队列 queue 存储当前层已生成的字符串组合，初始放入种子 [""]。
          2. 逐个遍历数字，按当前队列长度依次弹出上一层的字符串，与当前数字对应的每个字母拼接后重新入队。
          3. 遍历完所有数字后，队列中剩下的即为全部目标组合。
        - 复杂度：
          - 时间复杂度: O(3^m * 4^n) —— m、n 分别为对应 3 个和 4 个字母的数字个数
          - 空间复杂度: O(3^m * 4^n) —— 队列最多需存储最后一层的全部组合结果
        """
        if not digits:
            return []

        # 映射表：下标 0 和 1 空置，2~9 对应九宫格按键字母
        PHONE_MAP = ("", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")

        queue = deque([""])  # 初始放入空字符串种子

        for digit in digits:
            letters = PHONE_MAP[int(digit)]
            level_size = len(queue)

            for _ in range(level_size):
                curr = queue.popleft()  # 上一层字符串出队
                for char in letters:
                    queue.append(curr + char)  # 拼接新字符后重新入队

        return list(queue)

    # ================= 备选解法（供复习参考） =================
    # 方法二：DFS 回溯法 / 深度优先搜索
    # - 思路：自顶向下递归，index 表示当前处理的数字下标，path 记录当前路径组合；
    #         当 index == len(digits) 时收集结果并返回。
    # - 时间复杂度: O(3^m * 4^n)
    # - 空间复杂度: O(m + n) —— 递归调用栈深度取决于数字长度
    #
    # def letterCombinations_dfs(self, digits: str) -> List[str]:
    #     if not digits:
    #         return []
    #
    #     PHONE_MAP = ("", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")
    #     ans_list = []
    #
    #     def dfs(index: int, path: str):
    #         if index == len(digits):
    #             ans_list.append(path)
    #             return
    #         digit = digits[index]
    #         for s in PHONE_MAP[int(digit)]:
    #             dfs(index + 1, path + s)
    #
    #     dfs(0, "")
    #     return ans_list
    


# @lc code=end


#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#
