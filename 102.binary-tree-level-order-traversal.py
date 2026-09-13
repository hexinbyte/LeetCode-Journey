#
# @lc app=leetcode.cn id=102 lang=python3
# @lcpr version=30204
#
# [102] 二叉树的层序遍历
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
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        利用 BFS 双端队列进行二叉树层序遍历。
        - 时间复杂度: O(n) —— 每个节点进出队列一次
        - 空间复杂度: O(n) —— 队列最多容纳一层节点（最大宽度为 n/2）
        """
        node_list = deque()
        ans = []
        node_list.append(root)
        while node_list:
            size = len(node_list)
            t_ans = []
            for _ in range(size):
                t_node = node_list.popleft()
                if t_node:
                    t_ans.append(t_node.val)
                    node_list.append(t_node.left)
                    node_list.append(t_node.right)
            if t_ans:    
                ans.append(t_ans)

        return ans
                


        
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

