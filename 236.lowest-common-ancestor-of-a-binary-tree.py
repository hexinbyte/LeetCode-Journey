#
# @lc app=leetcode.cn id=236 lang=python3
# @lcpr version=30204
#
# [236] 二叉树的最近公共祖先
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        方法一：后序遍历 / 自底向上递归汇报（最优解）
        - 思路：
          1. 递归基底：遇到空节点或遇到 p、q，直接返回当前节点作为汇报信息。
          2. 分治搜索：自底向上递归，向左子树 left 和右子树 right 索取汇报。
          3. 决策合并：
             - 若 left 和 right 均非空：说明 p、q 分居两侧，当前 root 即为最近公共祖先，返回 root。
             - 若仅一侧非空：说明两者均在该侧（或该节点本身就是另一节点的祖先），继续将该侧非空节点向上透传汇报。
             - 若两侧均为空：说明均未找到，返回 None。
        - 复杂度：
          - 时间复杂度: O(n) —— 每个节点仅被访问一次
          - 空间复杂度: O(n) —— 递归栈深度，最坏情况下（树退化为链表）为 O(n)，平衡树为 O(log n)
        """
        # 1. 递归基底：到达空节点，或找到 p / q
        if not root or root == p or root == q:
            return root

        # 2. 自底向上分别向左右子树索取汇报
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        # 3. 左右两侧均有返回值，说明 p、q 分居两侧，当前 root 就是最近公共祖先
        if left and right:
            return root

        # 4. 仅一侧有值时，将该非空结果向上透传汇报；两边都空则返回 None
        return left if left else right

    # ================= 备选解法（供复习参考） =================
    # 方法二：自顶向下 BFS 层序遍历 + isAncestor 判定
    # - 思路：自顶向下层序遍历每个节点，调用 isAncestor 检查 p、q 是否在其子树中。
    # - 时间复杂度: O(n^2) —— 存在重复遍历
    # - 空间复杂度: O(n)
    #
    #     def isAncestor(t_root):
    #         if not t_root:
    #             return False
    #         if t_root == p or t_root == q:
    #             return True
    #         return isAncestor(t_root.left) or isAncestor(t_root.right)

    #     list = deque()
    #     list.append(root)
    #     ans = root
    #     while list:
    #         l = len(list)
    #         for _ in range(l):
    #             t = list.popleft()
    #             if (t == p or t == q) and (isAncestor(t.left) or isAncestor(t.right)):
    #                 ans = t
    #             elif isAncestor(t.left) and isAncestor(t.right):
    #                 ans = t
    #             if t.left:
    #                 list.append(t.left)
    #             if t.right:
    #                 list.append(t.right)
    #     return ans
        
# @lc code=end



#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n2\n
# @lcpr case=end

#

