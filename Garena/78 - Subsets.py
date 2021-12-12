class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first, curr, targetlen):
            if len(curr) == targetlen:
                output.append(curr[:])
                return
            for i in range(first, len(nums)):
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr, targetlen)
                curr.pop()

        output = []
        for k in range(len(nums) + 1):
            backtrack(0, [], k)

        return output