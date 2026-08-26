#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30204
#
# [2] 两数相加
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        核心思路：模拟加法（带剪枝优化）
        1. 使用 dummy 虚拟头节点构建新链表，carry 记录进位。
        2. 同步遍历两链表，累加当前节点值与进位。
        3. 利用 divmod(carry, 10) 快速更新进位（商）和当前位数字（余数）。
        4. 剪枝优化：若某一链表遍历完且无进位 (carry == 0)，直接拼接另一链表剩余部分并提前结束。
        
        复杂度分析：
        - 时间复杂度: O(max(m, n)) —— 最多遍历较长链表的长度
        - 空间复杂度: O(max(m, n)) —— 构建返回结果新链表所需的空间
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # 💡 剪枝优化：某链表为空且无进位时，直接接上另一链表并提前结束
            if not l1 and not carry:
                curr.next = l2
                break
            if not l2 and not carry:
                curr.next = l1
                break

            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            carry, val = divmod(carry, 10)
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

