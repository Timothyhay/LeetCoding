from typing import List
'''
为了防止回溯时“回头选数”产生重复排列，我们需要在递归时引入一个起始索引参数 start：
每层循环只从 candidates 的第 start 个位置开始向后遍历，不再向前看之前的元素。
题目允许同一个数字重复使用，所以在递归调用下一层时，传给下一层的起始索引依然是 i（而不是 i + 1）。
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int], remain: int):
            if remain < 0:
                return
            elif remain == 0:
                result.append(path.copy())
                return
            # 从 start 开始，避免回头选前面的数字导致生成重复组合
            for i in range(start, len(candidates)):
                c = candidates[i]
                path.append(c)
                # 传入 i 表示当前元素 c 还可以被重复选择
                backtrack(i, path, remain - c)
                path.pop()

        backtrack(0, [], target)
        return result


'''
总结比较
模式	           循环方式	                    递归传递索引	            适用场景
排列	           for c in candidates	        无	                    求全排列（允许/不允许重复元素）
组合（元素可复用）   for i in range(start, n)	    backtrack(i, ...)	    本题（Combination Sum）
组合（元素不可复用） for i in range(start, n)	    backtrack(i + 1, ...)	Combination Sum II / 子集问题

'''
