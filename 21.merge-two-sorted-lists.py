#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30204
#
# [21] 合并两个有序链表
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法一：双指针迭代 + 虚拟头节点（最优解）
        - 思路：
          1. 设虚拟头节点 head，当前指针 curr 指向 head。
          2. 当 list1 和 list2 均非空时，比较两节点的值，较小者接入 curr.next，并推进对应链表指针。
          3. 每次连接后推进 curr 指针（curr = curr.next）。
          4. 循环结束后，必有一个链表为空，直接将非空的另一个链表整条拼接到 curr.next。
        - 复杂度：
          - 时间复杂度: O(m + n) —— m 和 n 分别为两链表的长度，每个节点仅被遍历一次
          - 空间复杂度: O(1) —— 仅需常数个辅助指针
        """
        head = ListNode(0,None)
        curr = head
        # 1. 双指针比较较小值并接入新链表
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        # 2. 拼接剩余非空链表部分
        curr.next = list1 if list1 else list2

        return head.next
        
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

