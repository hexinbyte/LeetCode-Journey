#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30204
#
# [215] 数组中的第K个最大元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        基于三路划分 (Three-way Partition) 的快速选择 (Quickselect) 算法寻找第 K 大元素。
        - 时间复杂度: 平均 O(n)，最坏 O(n^2) —— 每次仅递归单侧分支，期望等比数列收敛
        - 空间复杂度: O(n) —— 递归各层新列表开销
        """
        #在nums 找第K大
        base = nums[len(nums) // 2]
        #小、相等、大
        left,middle,right = [],[],[]
        min_n,max_n = base,base
        for n in nums:
            if n < base:
                left.append(n)
                min_n = min (min_n,n)
            elif n > base:
                right.append(n)
                max_n = max (max_n,n)
            else:
                middle.append(n)
        if k == len(nums): return min_n
        if k == 1 : return max_n
        if k <= len(right): 
            return self.findKthLargest(right,k)
        elif k <= len(right)+len(middle):
            return base
        else:
            return self.findKthLargest(left,k-len(right)-len(middle))
        
# @lc code=end



#
# @lcpr case=start
# [3,2,1,5,6,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3,1,2,4,5,5,6]\n4\n
# @lcpr case=end

#

