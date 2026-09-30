#
# @lc app=leetcode.cn id=347 lang=python3
# @lcpr version=30204
#
# [347] 前 K 个高频元素
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        利用哈希表统计频次后进行桶排序，以出现次数作为桶下标，从高频向低频倒序遍历收集前 k 个元素。
        - 时间复杂度: O(n) —— 频次统计与桶遍历均为线性时间
        - 空间复杂度: O(n) —— 桶数组及哈希表占用线性空间
        """
        counts = Counter(nums)
        #buckets下标为次数，值为num
        buckets = [[] for _ in range(len(nums)+1)]
        for num,freq in counts.items():
            buckets[freq].append(num)
        ans = []
        for i in range(len(nums),0,-1):
            if buckets[i]:
                ans.extend(buckets[i])
            if len(ans) >= k:
                break

        return ans    

    # ================= 备选解法（供复习参考） =================
    # 方法二：双哈希表反向映射 + 频次排序
    # - 思路：先统计各数字频次，再建立反向哈希表按频次聚类数字，最后对频次列表降序排序依次提取前 k 个高频数。
    # - 时间复杂度: O(n + u log u) —— u 为不同频次种类数 (u <= sqrt(2n))，整体表现接近 O(n)
    # - 空间复杂度: O(n) —— 双哈希表存储所有数字及其频次映射
    #
    # def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    #     num_to_freq  = {}
    #     for num in nums:
    #         t = num_to_freq .get(num, 0)
    #         num_to_freq [num] = t + 1
    #     freq_to_nums = {}
    #     for key, value in num_to_freq .items():
    #         ts = freq_to_nums.get(value, [])
    #         ts.append(key)
    #         freq_to_nums[value] = ts

    #     ans = []
    #     freq_list = sorted(freq_to_nums.keys(),reverse=True)
    #     freq_list.sort(reverse=True)
    #     for v in freq_list:
    #         t = freq_to_nums[v]
    #         ans.extend(t)
    #         if len(ans) >= k:
    #             break
    #     return ans


# @lc code=end


#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,3,1,3,2]\n2\n
# @lcpr case=end

#
