# LeetCode Top 100 Liked & 代码随想录 重复题目分析

> 数据来源: LeetCode GraphQL API (Top 100 Liked, listId=79h8rn6) vs [代码随想录题单](https://programmercarl.com/qita/12.list.html)
> 分析日期: 2026-08-07

---

## 交集统计

- LeetCode Top 100 Liked: **100** 题
- 代码随想录题单(去重): **~140** 题
- 两源交集: **42** 题

**结论: 42/100 ≈ 42% 的 Top 100 Liked 题目在代码随想录中有覆盖。**

---

## 交集题目清单（按题号排序，共42题）

| # | 题号 | 题目 | 难度 | 代码随想录分类 |
|---|------|------|------|---------------|
| 1 | 1 | Two Sum | Easy | 哈希表 |
| 2 | 15 | 3Sum | Medium | 哈希表 / 双指针 |
| 3 | 17 | Letter Combinations of a Phone Number | Medium | 回溯算法 |
| 4 | 19 | Remove Nth Node From End of List | Medium | 链表 / 双指针 |
| 5 | 20 | Valid Parentheses | Easy | 栈和队列 |
| 6 | 24 | Swap Nodes in Pairs | Medium | 链表 |
| 7 | 39 | Combination Sum | Medium | 回溯算法 |
| 8 | 42 | Trapping Rain Water | Hard | 单调栈 |
| 9 | 45 | Jump Game II | Medium | 贪心 |
| 10 | 46 | Permutations | Medium | 回溯算法 |
| 11 | 51 | N-Queens | Hard | 回溯算法 |
| 12 | 53 | Maximum Subarray | Medium | 贪心 / 动态规划 |
| 13 | 55 | Jump Game | Medium | 贪心 |
| 14 | 56 | Merge Intervals | Medium | 贪心 |
| 15 | 62 | Unique Paths | Medium | 动态规划 |
| 16 | 70 | Climbing Stairs | Easy | 动态规划 |
| 17 | 72 | Edit Distance | Medium | 动态规划 |
| 18 | 78 | Subsets | Medium | 回溯算法 |
| 19 | 84 | Largest Rectangle in Histogram | Hard | 单调栈 |
| 20 | 94 | Binary Tree Inorder Traversal | Easy | 二叉树 |
| 21 | 98 | Validate Binary Search Tree | Medium | 二叉树 |
| 22 | 101 | Symmetric Tree | Easy | 二叉树 |
| 23 | 102 | Binary Tree Level Order Traversal | Medium | 二叉树 |
| 24 | 104 | Maximum Depth of Binary Tree | Easy | 二叉树 |
| 25 | 105 | Construct Binary Tree from Preorder and Inorder | Medium | 二叉树 |
| 26 | 121 | Best Time to Buy and Sell Stock | Easy | 动态规划 (股票) |
| 27 | 131 | Palindrome Partitioning | Medium | 回溯算法 |
| 28 | 139 | Word Break | Medium | 动态规划 |
| 29 | 142 | Linked List Cycle II | Medium | 链表 / 双指针 |
| 30 | 198 | House Robber | Medium | 动态规划 (打家劫舍) |
| 31 | 199 | Binary Tree Right Side View | Medium | 二叉树 |
| 32 | 206 | Reverse Linked List | Easy | 链表 / 双指针 |
| 33 | 226 | Invert Binary Tree | Easy | 二叉树 |
| 34 | 236 | Lowest Common Ancestor of a Binary Tree | Medium | 二叉树 |
| 35 | 239 | Sliding Window Maximum | Hard | 栈和队列 |
| 36 | 300 | Longest Increasing Subsequence | Medium | 动态规划 (子序列) |
| 37 | 322 | Coin Change | Medium | 动态规划 (完全背包) |
| 38 | 347 | Top K Frequent Elements | Medium | 栈和队列 |
| 39 | 416 | Partition Equal Subset Sum | Medium | 动态规划 (01背包) |
| 40 | 704 | Binary Search | Easy | 数组 |
| 41 | 739 | Daily Temperatures | Medium | 单调栈 |
| 42 | 1143 | Longest Common Subsequence | Medium | 动态规划 (子序列) |

---

## 按难度分布

| 难度 | 数量 |
|------|------|
| Easy | 11 |
| Medium | 27 |
| Hard | 4 |

---

## 按模块分布（Top 高频模块）

| 模块 | 题目数 | 占比 |
|------|--------|------|
| 动态规划 | 12 | 28.6% |
| 二叉树 | 8 | 19.0% |
| 回溯算法 | 6 | 14.3% |
| 链表 / 双指针 | 4 | 9.5% |
| 贪心 | 4 | 9.5% |
| 单调栈 | 3 | 7.1% |
| 栈和队列 | 3 | 7.1% |
| 哈希表 | 1 | 2.4% |
| 数组 | 1 | 2.4% |

---

## 备考优先级建议

### Tier 1 - 最高优先（两源交集 + Easy 起步）
这些是高频+基础题，考试出现概率极高：
- **1** Two Sum (Easy)
- **20** Valid Parentheses (Easy)
- **70** Climbing Stairs (Easy)
- **94** Binary Tree Inorder Traversal (Easy)
- **101** Symmetric Tree (Easy)
- **104** Maximum Depth of Binary Tree (Easy)
- **121** Best Time to Buy and Sell Stock (Easy)
- **206** Reverse Linked List (Easy)
- **226** Invert Binary Tree (Easy)
- **704** Binary Search (Easy)

### Tier 2 - 高频中等题（动态规划、二叉树、回溯）
- DP: 53, 62, 72, 139, 198, 300, 322, 416, 1143
- 二叉树: 98, 102, 105, 199, 236
- 回溯: 17, 39, 46, 78, 131
- 链表: 19, 24, 142

### Tier 3 - 高频困难题
- **42** Trapping Rain Water (Hard)
- **51** N-Queens (Hard)
- **84** Largest Rectangle in Histogram (Hard)
- **239** Sliding Window Maximum (Hard)

---

## Top 100 Liked 中未覆盖的高频题（补充练习）

以下题目在 Top 100 中但不在代码随想录题单中，建议额外关注：

| 题号 | 题目 | 难度 | 标签 |
|------|------|------|------|
| 2 | Add Two Numbers | Medium | 链表 |
| 3 | Longest Substring Without Repeating Characters | Medium | 滑动窗口 |
| 5 | Longest Palindromic Substring | Medium | DP / 双指针 |
| 11 | Container With Most Water | Medium | 双指针 |
| 21 | Merge Two Sorted Lists | Easy | 链表 |
| 22 | Generate Parentheses | Medium | 回溯 |
| 23 | Merge k Sorted Lists | Hard | 堆 / 分治 |
| 25 | Reverse Nodes in k-Group | Hard | 链表 |
| 33 | Search in Rotated Sorted Array | Medium | 二分 |
| 49 | Group Anagrams | Medium | 哈希 |
| 76 | Minimum Window Substring (在209页面推荐) | Hard | 滑动窗口 |
| 128 | Longest Consecutive Sequence | Medium | 哈希 |
| 141 | Linked List Cycle | Easy | 双指针 |
| 146 | LRU Cache | Medium | 设计 |
| 200 | Number of Islands | Medium | DFS/BFS |
| 207 | Course Schedule | Medium | 拓扑排序 |
| 208 | Implement Trie | Medium | Trie |
| 215 | Kth Largest Element in an Array | Medium | 堆 |
| 234 | Palindrome Linked List | Easy | 链表 |
| 238 | Product of Array Except Self | Medium | 前缀积 |
| 283 | Move Zeroes | Easy | 双指针 |
| 287 | Find the Duplicate Number | Medium | 双指针 |
| 394 | Decode String | Medium | 栈 |
| 438 | Find All Anagrams in a String | Medium | 滑动窗口 |
| 543 | Diameter of Binary Tree | Easy | 二叉树 |
| 560 | Subarray Sum Equals K | Medium | 前缀和+哈希 |
| 994 | Rotting Oranges | Medium | BFS |

---

## 时间紧张时的行动建议

1. **先做42道交集题** — 一题两吃，同时覆盖两个权威来源
2. **再做 Tier 1 的10道 Easy 题** 作为热身和信心建立
3. **最后做补充清单的高频题** — 尤其是 3(滑动窗口)、200(DFS)、146(LRU)、215(堆) 这些面试极高频题
4. 如果时间更紧，优先做 **动态规划 + 二叉树** 模块，因为这两块在交集中占比最高(47.6%)
