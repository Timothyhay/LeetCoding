# Backtracking
# 回溯法是解决这类组合问题最通用、最标准的方法。
# 它的核心思想是：逐个数字进行处理，对于当前数字对应的每个字母，我们将其加入当前组合中，然后递归处理下一个数字，
# 最后在回退（回溯）时将该字母移除，以便尝试其他分支。

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # 边界条件：如果输入为空，直接返回空列表
        if not digits:
            return []

        # 建立电话号码与字母的映射字典
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        combinations = []

        # 定义回溯函数
        def backtrack(index: int, current_path: list):
            # 基准情况（Base Case）：如果已经处理完了所有数字
            if index == len(digits):
                # 将当前字符列表拼接成字符串并存入结果
                combinations.append("".join(current_path))
                return

            # 获取当前数字对应的所有可能字母
            possible_letters = phone_map[digits[index]]

            # 遍历每个字母，进行回溯搜索
            for letter in possible_letters:
                current_path.append(letter)  # 做选择
                backtrack(index + 1, current_path)  # 进入下一层递归
                current_path.pop()  # 撤销选择（回溯）

        # 从第 0 个字符开始回溯，初始路径为空
        backtrack(0, [])
        return combinations