#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30204
#
# [234] 回文链表
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        方法一：快慢指针 + 就地反转后半部分（空间 O(1) 最优解）
        - 思路：
          1. 快慢指针找中点：fast 走两步，slow 走一步，循环结束后 slow 即为后半段的起点。
          2. 就地反转后半段：从 slow 开始就地反转链表（复用 206 题反转逻辑）。
          3. 双指针比对：cur 指向后半段反转后的头，head 指向前半段的头，同步遍历逐值比对。
        - 复杂度：
          - 时间复杂度: O(n) —— 找中点、反转、比对各遍历半程，总体时间复杂度为 O(n)
          - 空间复杂度: O(1) —— 仅需常数个指针变量就地反转，无需额外数组或栈
        """
        # 1. 快慢指针定位链表中点
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 就地反转后半段链表
        cur = None
        while slow:
            next_node = slow.next
            slow.next = cur
            cur = slow
            slow = next_node

        # 3. 前后两半段双指针同步比对
        while cur and head:
            if cur.val != head.val:
                return False
            cur = cur.next
            head = head.next

        return True

    # ================= 备选解法（供复习参考） =================
    # 方法二：快慢指针 + 栈匹配
    # - 思路：快慢指针遍历找中点的同时将前半段节点值压栈；跳过奇数中心点后，slow 继续向后遍历并与栈顶弹出值逐一比对。
    # - 时间复杂度: O(n)
    # - 空间复杂度: O(n) —— 栈需存储前半段节点的值
    #
    #     slow,fast = head,head
    #     stack = []
    #     while fast and fast.next:
    #         stack.append(slow.val)
    #         slow = slow.next
    #         fast = fast.next.next

    #     if fast:
    #         slow = slow.next

    #     while slow:
    #         if slow.val != stack.pop():
    #             return False
    #         slow = slow.next

    #     return True

        
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

