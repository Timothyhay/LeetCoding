# Backtracking
# 在这道题中，我们要生成 n 对括号的所有合法的组合。长度为 2n 的合法括号组合在构建过程中必须满足以下两个核心规律（即约束条件）：
# 左括号的数量：在任何时候，左括号的数量都不能超过 n
# 右括号的数量：在任何时候，右括号的数量都不能超过当前已有的左括号数量。如果右括号多于左括号，组合必然非法（例如 ()) 无法再通过后续补齐变成合法组合）。

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        # open_count: 当前已使用的左括号数量
        # close_count: 当前已使用的右括号数量
        # path: 记录当前路径上的括号字符列表
        def backtrack(open_count: int, close_count: int, path: list):
            # 基准情况：当路径长度达到 2 * n 时，说明找到了一个完整合法的组合
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            # 尝试添加左括号：只要左括号数量小于 n 就可以添加
            if open_count < n:
                path.append('(')
                backtrack(open_count + 1, close_count, path)
                path.pop()  # 回溯，撤销选择

            # 尝试添加右括号：只要右括号数量小于左括号数量，就可以添加
            if close_count < open_count:
                path.append(')')
                backtrack(open_count, close_count + 1, path)
                path.pop()  # 回溯，撤销选择

        backtrack(0, 0, [])
        return res