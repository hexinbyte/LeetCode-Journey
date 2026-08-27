#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        方法一：双指针归并模拟法（推荐掌握，逻辑清晰实用）
        - 思路：
          1. 模拟归并排序的双指针移动，指针 i 和 j 分别指向两数组头部。
          2. 使用 prev 和 curr 两个滚动变量记录当前和上一个遍历到的数值。
          3. 循环遍历 (m + n) // 2 + 1 次（无论奇偶，刚好覆盖到中位数所需位置）：
             - 满足 i < m 且 (j >= n 或 nums1[i] <= nums2[j]) 时，取 nums1[i] 并后移 i；
             - 否则取 nums2[j] 并后移 j。
          4. 最终：
             - 长度为奇数：直接返回 float(curr)；
             - 长度为偶数：返回 (prev + curr) / 2.0。
             
        复杂度分析：
        - 时间复杂度: O(m + n) —— 仅遍历数组长度的一半
        - 空间复杂度: O(1) —— 仅使用常数个辅助变量
        """
        m, n = len(nums1), len(nums2)
        total = m + n

        i, j = 0, 0
        prev, curr = 0, 0

        for _ in range(total // 2 + 1):
            prev = curr

            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if total % 2 == 0:
            return (prev + curr) / 2.0
        else:
            return float(curr)

    # ================= 备选解法（供进阶复习参考） =================
    # 方法二：二分查找 / 寻找第 k 小元素（排除法，达到 O(log(m+n)) 进阶要求）
    # - 思路：每次比较两数组当前偏移后第 k//2 个元素，将较小者前 k//2 个元素淘汰排除
    # - 时间复杂度: O(log(m + n))
    # - 空间复杂度: O(1)
    #
    # def findMedianSortedArrays_kth(self, nums1: List[int], nums2: List[int]) -> float:
    #     def getKthElement(k: int) -> int:
    #         index1, index2 = 0, 0
    #         while True:
    #             if index1 == m:
    #                 return nums2[index2 + k - 1]
    #             if index2 == n:
    #                 return nums1[index1 + k - 1]
    #             if k == 1:
    #                 return min(nums1[index1], nums2[index2])
    #
    #             newIndex1 = min(index1 + k // 2 - 1, m - 1)
    #             newIndex2 = min(index2 + k // 2 - 1, n - 1)
    #             pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
    #             if pivot1 <= pivot2:
    #                 k -= newIndex1 - index1 + 1
    #                 index1 = newIndex1 + 1
    #             else:
    #                 k -= newIndex2 - index2 + 1
    #                 index2 = newIndex2 + 1
    #
    #     m, n = len(nums1), len(nums2)
    #     totalLength = m + n
    #     if totalLength % 2 == 1:
    #         return float(getKthElement((totalLength + 1) // 2))
    #     else:
    #         mid1 = getKthElement(totalLength // 2)
    #         mid2 = getKthElement(totalLength // 2 + 1)
    #         return (mid1 + mid2) / 2.0
# @lc code=end


#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#
