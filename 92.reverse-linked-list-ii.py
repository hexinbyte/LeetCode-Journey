#
# @lc app=leetcode.cn id=92 lang=python3
# @lcpr version=30204
#
# [92] 反转链表 II
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
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        """
        哨兵节点 + 迭代局部反转：利用 dummy 节点定位反转起点前驱，局部反转区间链表后重新缝合头尾。
        - 时间复杂度: O(n) —— 仅需单次遍历至第 right 个节点
        - 空间复杂度: O(1) —— 仅使用常数个指针变量原地修改指针
        """
        dummy = ListNode(None,head)
        p0 = dummy
        #先走到要反转的地方
        for _ in range(left-1):
            p0 = p0.next
        #进行反转
        pre = None
        cur = p0.next
        for _ in range(right - left +1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        #处理最后的节点连接情况
        p0.next.next = cur
        p0.next = pre

        return dummy.next
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#

