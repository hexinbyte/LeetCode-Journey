#
# @lc app=leetcode.cn id=206 lang=python3
# @lcpr version=30204
#
# [206] 反转链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法一：双指针尾递归（递归反转）
        - 思路：
          1. 定义递归函数 dfs(prev, curr)，其中 prev 为已反转部分的新头节点，curr 为当前待反转节点。
          2. 递归出口：当 curr 为空时，说明已到达原链表末尾，prev 即为反转后的新链表头节点，直接返回。
          3. 递归推进：暂存 next = curr.next，反转指针 curr.next = prev，递归调用 dfs(curr, next)。
        - 复杂度：
          - 时间复杂度: O(n) —— 链表长度为 n，需遍历 n 次
          - 空间复杂度: O(n) —— 递归调用栈的最大深度为 n
        """
        def dfs(prev,curr):
            if not curr:
                return prev
            next = curr.next
            curr.next = prev
            return dfs(curr,next)

        return dfs(None,head)

    # ================= 备选解法（供复习参考） =================
    # 方法二：双指针迭代法（经典空间 O(1) 最优解）
    # - 思路：slow 指针从 None 开始，right 指针从 head 开始遍历；
    #         逐个反转指针指向（right.next = slow），并同步向后推进 slow 和 right。
    # - 时间复杂度: O(n)
    # - 空间复杂度: O(1)
    #
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     slow = None
    #     right = head
    #     while right:
    #         next = right.next
    #         right.next = slow
    #         slow = right
    #         right = next
    #     return slow


        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

