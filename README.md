# 💡 LeetCode-Journey

> 记录个人 LeetCode 刷题历程与算法沉淀。保持思考，持续精进！

[![Language](https://img.shields.io/badge/Language-Python%203-blue.svg)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/Platform-LeetCode-FFA116.svg?logo=leetcode)](https://leetcode.cn/)

---

## 📚 刷题索引

| 题号 | 题目名称 | 难度 | 核心解法 / 算法标签 | 时间复杂度 | 空间复杂度 | 题解代码 |
| :---: | :--- | :---: | :--- | :---: | :---: | :---: |
| 0001 | [两数之和](https://leetcode.cn/problems/two-sum/) | 🟢 简单 | 哈希表 (Hash Map) | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | [1.two-sum.py](./1.two-sum.py) |
| 0002 | [两数相加](https://leetcode.cn/problems/add-two-numbers/) | 🟡 中等 | 模拟 / 链表 / 剪枝 | $\mathcal{O}(\max(m, n))$ | $\mathcal{O}(\max(m, n))$ | [2.add-two-numbers.py](./2.add-two-numbers.py) |
| 0003 | [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) | 🟡 中等 | 滑动窗口 / 哈希表 / 双指针 | $\mathcal{O}(n)$ | $\mathcal{O}(\vert\Sigma\vert)$ | [3.longest-substring-without-repeating-characters.py](./3.longest-substring-without-repeating-characters.py) |
| 0004 | [寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/) | 🔴 困难 | 二分查找 / 寻找第 k 小元素 / 双指针 | $\mathcal{O}(\log(m + n))$ | $\mathcal{O}(1)$ | [4.median-of-two-sorted-arrays.py](./4.median-of-two-sorted-arrays.py) |

---

## 📂 目录结构

```text
LeetCode-Journey/
├── 1.two-sum.py       # [题号].[题目英文名].py
├── README.md          # 刷题索引与记录
└── ...
```

---

## 📈 算法分类速查

- **基础**：数组、哈希表、双指针、滑动窗口、二分查找
- **进阶**：链表、栈与队列、二叉树、回溯、贪心
- **高阶**：动态规划、图论、并查集、单调栈