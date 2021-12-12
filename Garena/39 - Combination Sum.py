from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        # Add a remain to param to deduce calculation cost
        def backtrack(first=0, curr=[], remain=target):
            if remain < 0:
                return
            if remain == 0:
                output.append(curr[:])
                # print("output:",output, "Curr:", curr)
                return

            for i in range(first, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr, remain - candidates[i])
                curr.pop()



        backtrack(0, [], target)
        return output



if __name__ == '__main__':
    S = Solution()
    print(S.combinationSum([2,3,6,7], 7))

