class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cost = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        cost[0][0] = grid[0][0]

        for row in range(1, len(grid)):
            cost[row][0] = cost[row-1][0] + grid[row][0]

        for col in range(1, len(grid[0])):
            cost[0][col] = cost[0][col-1] + grid[0][col]


        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                cost[row][col] = min(cost[row-1][col], cost[row][col-1]) + grid[row][col]

        return cost[len(grid)-1][len(grid[0])-1]

