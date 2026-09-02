#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30204
#
# [19] 删除链表的倒数第 N 个结点
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        方法一：快慢双指针（一趟扫描，最优解）
        - 思路：
          1. 设 dummy 哑节点指向 head，统一删除头节点等边界情况。
          2. fast 指针先走 n + 1 步，与 slow 保持固定间距。
          3. fast 和 slow 同速前进，当 fast 走到末尾 None 时，slow 恰好指向待删节点的前驱节点。
          4. 通过 slow.next = slow.next.next 跨过并删除目标节点。
        - 复杂度：
          - 时间复杂度: O(L) —— L 为链表长度，仅需一趟遍历
          - 空间复杂度: O(1) —— 仅使用常数个辅助指针
        """
        dummy = ListNode(0,head)
        slow, fast = dummy, dummy
        # fast 先走 n + 1 步拉开间距
        for _ in range(n+1):
            fast = fast.next

        # 双指针同步前进，直至 fast 越过链表末尾
        while fast:
            fast = fast.next
            slow = slow.next

        # 删除倒数第 n 个节点
        slow.next = slow.next.next

        return dummy.next

    # ================= 备选解法（供复习参考） =================
    # 方法二：计算链表长度（两趟扫描）
    # - 思路：第一趟遍历统计链表总长度 sz；第二趟从 dummy 出发走 sz - n 步找到前驱节点并执行删除。
    # - 时间复杂度: O(L) —— 遍历两遍链表
    # - 空间复杂度: O(1)
    #
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     sz = 0
    #     thead = head
    #     while thead:
    #         thead = thead.next
    #         sz += 1
    #
    #     pre = ListNode(0,head)
    #
    #     left = pre
    #     for _ in range(sz - n):
    #         left = left.next
    #
    #     right = left
    #     for _ in range(2):
    #         if right is None:
    #             break
    #         right = right.next
  
    #     left.next = right
    #     return pre.next
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

