#
# @lc app=leetcode.cn id=104 lang=python3
# @lcpr version=30204
#
# [104] 二叉树的最大深度
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
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        利用 DFS 深度优先搜索（先序遍历）自顶向下传递当前深度。
        - 时间复杂度: O(n) —— 每个二叉树节点遍历一次
        - 空间复杂度: O(n) —— 最坏退化为链状树时递归栈深度为 n，平衡树时为 O(log n)
        """
        ans = float('-inf')
        def dfs(t_root,deep):
            nonlocal ans
            if not t_root:
                ans = max(ans,deep)
            else:
                dfs(t_root.left,deep+1)
                dfs(t_root.right,deep+1)

        
        dfs(root,0)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#

