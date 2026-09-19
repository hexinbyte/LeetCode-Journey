#
# @lc app=leetcode.cn id=124 lang=python3
# @lcpr version=30204
#
# [124] 二叉树中的最大路径和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        """
        利用后序遍历自底向上递归计算左右子树的最大单侧增益（负贡献舍弃置为 0）。
        在每个节点处计算包含当前节点的完整倒 V 形路径和以更新全局最大值，向上仅返回单侧最大延伸路径。
        - 时间复杂度: O(n) —— 每个二叉树节点恰好访问一次
        - 空间复杂度: O(n) —— 最坏退化为单链时递归栈深度为 n，平衡二叉树时为 O(log n)
        """
        ans_max = float("-inf")

        def dfs(node):
            nonlocal ans_max

            if not node:
                return 0
            # 左边的最大和，若小于0则做0处理，即抛去
            left_gain = max(0, dfs(node.left))
            # 右边的最大和，若小于0则做0处理，即抛去
            right_gain = max(0, dfs(node.right))

            # 比较一下，此节点作为中间倒V节点的最大路径和
            ans_max = max(ans_max, node.val + left_gain + right_gain)

            # 返回此节点作为头节点的最大和
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return ans_max


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-10,9,20,null,null,15,7]\n
# @lcpr case=end

#
