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

| # | 题号 | 题目 | 难度 | 代码随想录分类 | 题解链接 |
|---|------|------|------|---------------|---------|
| 1 | 1 | Two Sum | Easy | 哈希表 | [/algo/hash-table/0001-two-sum.html](https://programmercarl.com/algo/hash-table/0001-two-sum.html) |
| 2 | 15 | 3Sum | Medium | 哈希表 / 双指针 | [/algo/hash-table/0015-3sum.html](https://programmercarl.com/algo/hash-table/0015-3sum.html) |
| 3 | 17 | Letter Combinations of a Phone Number | Medium | 回溯算法 | [/algo/backtracking/0017-letter-combinations-of-a-phone-number.html](https://programmercarl.com/algo/backtracking/0017-letter-combinations-of-a-phone-number.html) |
| 4 | 19 | Remove Nth Node From End of List | Medium | 链表 / 双指针 | [/algo/linked-list/0019-remove-nth-node-from-end-of-list.html](https://programmercarl.com/algo/linked-list/0019-remove-nth-node-from-end-of-list.html) |
| 5 | 20 | Valid Parentheses | Easy | 栈和队列 | [/algo/stack-queue/0020-valid-parentheses.html](https://programmercarl.com/algo/stack-queue/0020-valid-parentheses.html) |
| 6 | 24 | Swap Nodes in Pairs | Medium | 链表 | [/algo/linked-list/0024-swap-nodes-in-pairs.html](https://programmercarl.com/algo/linked-list/0024-swap-nodes-in-pairs.html) |
| 7 | 39 | Combination Sum | Medium | 回溯算法 | [/algo/backtracking/0039-combination-sum.html](https://programmercarl.com/algo/backtracking/0039-combination-sum.html) |
| 8 | 42 | Trapping Rain Water | Hard | 单调栈 | [/algo/monotonic-stack/0042-trapping-rain-water.html](https://programmercarl.com/algo/monotonic-stack/0042-trapping-rain-water.html) |
| 9 | 45 | Jump Game II | Medium | 贪心 | [/algo/greedy/0045-jump-game-ii.html](https://programmercarl.com/algo/greedy/0045-jump-game-ii.html) |
| 10 | 46 | Permutations | Medium | 回溯算法 | [/algo/backtracking/0046-permutations.html](https://programmercarl.com/algo/backtracking/0046-permutations.html) |
| 11 | 51 | N-Queens | Hard | 回溯算法 | [/algo/backtracking/0051-n-queens.html](https://programmercarl.com/algo/backtracking/0051-n-queens.html) |
| 12 | 53 | Maximum Subarray | Medium | 贪心 / 动态规划 | [/algo/greedy/0053-maximum-subarray.html](https://programmercarl.com/algo/greedy/0053-maximum-subarray.html) |
| 13 | 55 | Jump Game | Medium | 贪心 | [/algo/greedy/0055-jump-game.html](https://programmercarl.com/algo/greedy/0055-jump-game.html) |
| 14 | 56 | Merge Intervals | Medium | 贪心 | [/algo/greedy/0056-merge-intervals.html](https://programmercarl.com/algo/greedy/0056-merge-intervals.html) |
| 15 | 62 | Unique Paths | Medium | 动态规划 | [/algo/dynamic-programming/0062-unique-paths.html](https://programmercarl.com/algo/dynamic-programming/0062-unique-paths.html) |
| 16 | 70 | Climbing Stairs | Easy | 动态规划 | [/algo/dynamic-programming/0070-climbing-stairs.html](https://programmercarl.com/algo/dynamic-programming/0070-climbing-stairs.html) |
| 17 | 72 | Edit Distance | Medium | 动态规划 | [/algo/dynamic-programming/0072-edit-distance.html](https://programmercarl.com/algo/dynamic-programming/0072-edit-distance.html) |
| 18 | 78 | Subsets | Medium | 回溯算法 | [/algo/backtracking/0078-subsets.html](https://programmercarl.com/algo/backtracking/0078-subsets.html) |
| 19 | 84 | Largest Rectangle in Histogram | Hard | 单调栈 | [/algo/monotonic-stack/0084-largest-rectangle-in-histogram.html](https://programmercarl.com/algo/monotonic-stack/0084-largest-rectangle-in-histogram.html) |
| 20 | 94 | Binary Tree Inorder Traversal | Easy | 二叉树 | 见递归/迭代遍历页 (见下方备注) |
| 21 | 98 | Validate Binary Search Tree | Medium | 二叉树 | [/algo/binary-tree/0098-validate-binary-search-tree.html](https://programmercarl.com/algo/binary-tree/0098-validate-binary-search-tree.html) |
| 22 | 101 | Symmetric Tree | Easy | 二叉树 | [/algo/binary-tree/0101-symmetric-tree.html](https://programmercarl.com/algo/binary-tree/0101-symmetric-tree.html) |
| 23 | 102 | Binary Tree Level Order Traversal | Medium | 二叉树 | [/algo/binary-tree/0102-binary-tree-level-order-traversal.html](https://programmercarl.com/algo/binary-tree/0102-binary-tree-level-order-traversal.html) |
| 24 | 104 | Maximum Depth of Binary Tree | Easy | 二叉树 | [/algo/binary-tree/0104-maximum-depth-of-binary-tree.html](https://programmercarl.com/algo/binary-tree/0104-maximum-depth-of-binary-tree.html) |
| 25 | 105 | Construct Binary Tree from Preorder and Inorder | Medium | 二叉树 | [/algo/binary-tree/0105-construct-binary-tree-from-preorder-and-inorder-traversal.html](https://programmercarl.com/algo/binary-tree/0105-construct-binary-tree-from-preorder-and-inorder-traversal.html) |
| 26 | 121 | Best Time to Buy and Sell Stock | Easy | 动态规划 (股票) | [/algo/dynamic-programming/0121-best-time-to-buy-and-sell-stock.html](https://programmercarl.com/algo/dynamic-programming/0121-best-time-to-buy-and-sell-stock.html) |
| 27 | 131 | Palindrome Partitioning | Medium | 回溯算法 | [/algo/backtracking/0131-palindrome-partitioning.html](https://programmercarl.com/algo/backtracking/0131-palindrome-partitioning.html) |
| 28 | 139 | Word Break | Medium | 动态规划 | [/algo/dynamic-programming/0139-word-break.html](https://programmercarl.com/algo/dynamic-programming/0139-word-break.html) |
| 29 | 142 | Linked List Cycle II | Medium | 链表 / 双指针 | [/algo/linked-list/0142-linked-list-cycle-ii.html](https://programmercarl.com/algo/linked-list/0142-linked-list-cycle-ii.html) |
| 30 | 198 | House Robber | Medium | 动态规划 (打家劫舍) | [/algo/dynamic-programming/0198-house-robber.html](https://programmercarl.com/algo/dynamic-programming/0198-house-robber.html) |
| 31 | 199 | Binary Tree Right Side View | Medium | 二叉树 | [/algo/binary-tree/0199-binary-tree-right-side-view.html](https://programmercarl.com/algo/binary-tree/0199-binary-tree-right-side-view.html) |
| 32 | 206 | Reverse Linked List | Easy | 链表 / 双指针 | [/algo/linked-list/0206-reverse-linked-list.html](https://programmercarl.com/algo/linked-list/0206-reverse-linked-list.html) |
| 33 | 226 | Invert Binary Tree | Easy | 二叉树 | [/algo/binary-tree/0226-invert-binary-tree.html](https://programmercarl.com/algo/binary-tree/0226-invert-binary-tree.html) |
| 34 | 236 | Lowest Common Ancestor of a Binary Tree | Medium | 二叉树 | [/algo/binary-tree/0236-lowest-common-ancestor-of-a-binary-tree.html](https://programmercarl.com/algo/binary-tree/0236-lowest-common-ancestor-of-a-binary-tree.html) |
| 35 | 239 | Sliding Window Maximum | Hard | 栈和队列 | [/algo/stack-queue/0239-sliding-window-maximum.html](https://programmercarl.com/algo/stack-queue/0239-sliding-window-maximum.html) |
| 36 | 300 | Longest Increasing Subsequence | Medium | 动态规划 (子序列) | [/algo/dynamic-programming/0300-longest-increasing-subsequence.html](https://programmercarl.com/algo/dynamic-programming/0300-longest-increasing-subsequence.html) |
| 37 | 322 | Coin Change | Medium | 动态规划 (完全背包) | [/algo/dynamic-programming/0322-coin-change.html](https://programmercarl.com/algo/dynamic-programming/0322-coin-change.html) |
| 38 | 347 | Top K Frequent Elements | Medium | 栈和队列 | [/algo/stack-queue/0347-top-k-frequent-elements.html](https://programmercarl.com/algo/stack-queue/0347-top-k-frequent-elements.html) |
| 39 | 416 | Partition Equal Subset Sum | Medium | 动态规划 (01背包) | [/algo/dynamic-programming/0416-partition-equal-subset-sum.html](https://programmercarl.com/algo/dynamic-programming/0416-partition-equal-subset-sum.html) |
| 40 | 704 | Binary Search | Easy | 数组 | [/algo/array/0704-binary-search.html](https://programmercarl.com/algo/array/0704-binary-search.html) |
| 41 | 739 | Daily Temperatures | Medium | 单调栈 | [/algo/monotonic-stack/0739-daily-temperatures.html](https://programmercarl.com/algo/monotonic-stack/0739-daily-temperatures.html) |
| 42 | 1143 | Longest Common Subsequence | Medium | 动态规划 (子序列) | [/algo/dynamic-programming/1143-longest-common-subsequence.html](https://programmercarl.com/algo/dynamic-programming/1143-longest-common-subsequence.html) |

> **备注**: #94 二叉树的中序遍历在代码随想录中未设独立页面，而是合并在以下三篇遍历专题中:
> - [二叉树的递归遍历](https://programmercarl.com/algo/binary-tree/binary-tree-recursive-traversal.html)
> - [二叉树的迭代遍历](https://programmercarl.com/algo/binary-tree/binary-tree-iterative-traversal.html)
> - [二叉树的统一迭代法](https://programmercarl.com/algo/binary-tree/binary-tree-unified-iterative-traversal.html)

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
- **1** [Two Sum](https://programmercarl.com/algo/hash-table/0001-two-sum.html) (Easy)
- **20** [Valid Parentheses](https://programmercarl.com/algo/stack-queue/0020-valid-parentheses.html) (Easy)
- **70** [Climbing Stairs](https://programmercarl.com/algo/dynamic-programming/0070-climbing-stairs.html) (Easy)
- **94** Binary Tree Inorder Traversal (Easy) → 见[遍历专题](https://programmercarl.com/algo/binary-tree/binary-tree-iterative-traversal.html)
- **101** [Symmetric Tree](https://programmercarl.com/algo/binary-tree/0101-symmetric-tree.html) (Easy)
- **104** [Maximum Depth of Binary Tree](https://programmercarl.com/algo/binary-tree/0104-maximum-depth-of-binary-tree.html) (Easy)
- **121** [Best Time to Buy and Sell Stock](https://programmercarl.com/algo/dynamic-programming/0121-best-time-to-buy-and-sell-stock.html) (Easy)
- **206** [Reverse Linked List](https://programmercarl.com/algo/linked-list/0206-reverse-linked-list.html) (Easy)
- **226** [Invert Binary Tree](https://programmercarl.com/algo/binary-tree/0226-invert-binary-tree.html) (Easy)
- **704** [Binary Search](https://programmercarl.com/algo/array/0704-binary-search.html) (Easy)

### Tier 2 - 高频中等题

**动态规划**:
- [53. Maximum Subarray](https://programmercarl.com/algo/greedy/0053-maximum-subarray.html)
- [62. Unique Paths](https://programmercarl.com/algo/dynamic-programming/0062-unique-paths.html)
- [72. Edit Distance](https://programmercarl.com/algo/dynamic-programming/0072-edit-distance.html)
- [139. Word Break](https://programmercarl.com/algo/dynamic-programming/0139-word-break.html)
- [198. House Robber](https://programmercarl.com/algo/dynamic-programming/0198-house-robber.html)
- [300. Longest Increasing Subsequence](https://programmercarl.com/algo/dynamic-programming/0300-longest-increasing-subsequence.html)
- [322. Coin Change](https://programmercarl.com/algo/dynamic-programming/0322-coin-change.html)
- [416. Partition Equal Subset Sum](https://programmercarl.com/algo/dynamic-programming/0416-partition-equal-subset-sum.html)
- [1143. Longest Common Subsequence](https://programmercarl.com/algo/dynamic-programming/1143-longest-common-subsequence.html)

**二叉树**:
- [98. Validate Binary Search Tree](https://programmercarl.com/algo/binary-tree/0098-validate-binary-search-tree.html)
- [102. Binary Tree Level Order Traversal](https://programmercarl.com/algo/binary-tree/0102-binary-tree-level-order-traversal.html)
- [105. Construct Binary Tree from Preorder and Inorder](https://programmercarl.com/algo/binary-tree/0105-construct-binary-tree-from-preorder-and-inorder-traversal.html)
- [199. Binary Tree Right Side View](https://programmercarl.com/algo/binary-tree/0199-binary-tree-right-side-view.html)
- [236. Lowest Common Ancestor of a Binary Tree](https://programmercarl.com/algo/binary-tree/0236-lowest-common-ancestor-of-a-binary-tree.html)

**回溯算法**:
- [15. 3Sum](https://programmercarl.com/algo/hash-table/0015-3sum.html)
- [17. Letter Combinations of a Phone Number](https://programmercarl.com/algo/backtracking/0017-letter-combinations-of-a-phone-number.html)
- [39. Combination Sum](https://programmercarl.com/algo/backtracking/0039-combination-sum.html)
- [46. Permutations](https://programmercarl.com/algo/backtracking/0046-permutations.html)
- [78. Subsets](https://programmercarl.com/algo/backtracking/0078-subsets.html)
- [131. Palindrome Partitioning](https://programmercarl.com/algo/backtracking/0131-palindrome-partitioning.html)

**链表/双指针 + 贪心 + 其他**:
- [19. Remove Nth Node From End](https://programmercarl.com/algo/linked-list/0019-remove-nth-node-from-end-of-list.html)
- [24. Swap Nodes in Pairs](https://programmercarl.com/algo/linked-list/0024-swap-nodes-in-pairs.html)
- [142. Linked List Cycle II](https://programmercarl.com/algo/linked-list/0142-linked-list-cycle-ii.html)
- [55. Jump Game](https://programmercarl.com/algo/greedy/0055-jump-game.html)
- [56. Merge Intervals](https://programmercarl.com/algo/greedy/0056-merge-intervals.html)

### Tier 3 - 高频困难题
- **[42. Trapping Rain Water](https://programmercarl.com/algo/monotonic-stack/0042-trapping-rain-water.html)** (Hard)
- **[51. N-Queens](https://programmercarl.com/algo/backtracking/0051-n-queens.html)** (Hard)
- **[84. Largest Rectangle in Histogram](https://programmercarl.com/algo/monotonic-stack/0084-largest-rectangle-in-histogram.html)** (Hard)
- **[239. Sliding Window Maximum](https://programmercarl.com/algo/stack-queue/0239-sliding-window-maximum.html)** (Hard)

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

1. **先做42道交集题** — 一题两吃，同时覆盖两个权威来源，每题都有代码随想录详解题解
2. **再做 Tier 1 的10道 Easy 题** 作为热身和信心建立
3. **最后做补充清单的高频题** — 尤其是 3(滑动窗口)、200(DFS)、146(LRU)、215(堆) 这些面试极高频题
4. 如果时间更紧，优先做 **动态规划 + 二叉树** 模块，因为这两块在交集中占比最高(47.6%)
