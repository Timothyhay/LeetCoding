# Hash Table
'''
LeetCode 560. 和为 K 的子数组（Subarray Sum Equals K） 是一道非常经典的算法题。

解决这道题的最优解法是使用 前缀和（Prefix Sum）+ 哈希表（Hash Map），时间复杂度可以达到 O(N)。

一、核心思路推导

1.  什么是前缀和？ 设 preSum[i] 表示数组中从第 0 个元素累加到第 i 个元素的和（即 nums[0] + nums[1] + ... +
    nums[i]）。

2.  如何求任意区间 [j, i] 的子数组和？ 区间 [j, i] 的子数组和为：
    subarray_sum(j, i) = preSum[i] - preSum[j - 1]

3.  转化问题： 题目要求找到和为 k 的子数组，即寻找满足下式的区间：
    preSum[i] - preSum[j - 1] = k 把公式稍微变形一下得到：
    preSum[j - 1] = preSum[i] - k

    这意味着：当我们遍历到位置 i（当前前缀和为 preSum[i]）时，只需要知道在此之前，有多少个位置的前缀和等于
    preSum[i] - k 即可。

4.  利用哈希表加速查找： 我们可以用一个哈希表 prefix_map 来记录某个前缀和出现的次数：

      - Key：前缀和的值
      - Value：该前缀和出现的次数

二、算法步骤

1.  初始化一个哈希表 prefix_map，并写入 {0: 1}（解释见下方注意点）。
2.  初始化变量 current_sum = 0（记录当前前缀和）以及 count = 0（记录和为 k 的子数组个数）。
3.  遍历数组中的每一个数字 num：
      - 将 num 累加到 current_sum 中。
      - 检查 current_sum - k 是否存在于哈希表中：
          - 如果存在，说明找到了若干个以当前数字结尾的子数组，其和为 k。将哈希表中对应的次数加到 count 上。
      - 将当前的前缀和 current_sum 存入哈希表中（若已存在则频次 +1）。
4.  遍历结束，返回 count。
'''


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        # 哈希表存储 {前缀和: 出现的次数}
        # 初始放入 {0: 1}，用于处理当前前缀和直接等于 k 的情况
        prefix_map = {0: 1}

        for num in nums:
            current_sum += num

            # 如果 current_sum - k 存在，累加其出现的次数
            if (current_sum - k) in prefix_map:
                count += prefix_map[current_sum - k]

            # 更新当前前缀和的频次
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

        return count