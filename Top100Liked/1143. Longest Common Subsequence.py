class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        千万不要使用乘法复制二维列表
        # WRONG WAY! 错误写法！
        dp = [[0] * (n + 1)] * (m + 1)
        为什么是错的？
        外层的 * (m + 1) 并没有创建新的列表，而是将同一个内层列表的引用（内存地址）复制了 m + 1 次。
        当你修改某一行时，所有行都会同时改变。
        '''
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        '''
        m, n = len(text1), len(text2)
        [0] * (n + 1)：先做出一根长度为 n + 1 的“横条”（即一整行的所有列）。
        for _ in range(m + 1)：把这个横条复制 m + 1 份叠起来（即一共有多少行）。

        访问/遍历时：先行后列
        访问永远是 dp[行][列] → dp[i][j]
        既然先确定行，外层循环必须是行号 i（范围是总行数 m + 1）；
        内层循环是列号 j（范围是总列数 n + 1）。
        '''
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    # DP 数组大小是 (m + 1) * (n + 1)，其中 dp[i + 1][j + 1] 表示 text1[0...i] 和 text2[0...j] 的最长公共子序列长度。
                    # 当字符不相等（text1[i] != text2[j]）时，应该取以下两种情况的最大值：
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[-1][-1]
