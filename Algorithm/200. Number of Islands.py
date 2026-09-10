class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def mark_neighbor_land(grid, pos_x, pos_y):
            if pos_x < 0 or pos_x >= len(grid):
                return
            if pos_y < 0 or pos_y >= len(grid[0]):
                return
            # 如果当前格子不是 '1'（是水 '0' 或者已经访问过的 '0'/'-1'），直接返回
            # 注意这里不能是 grid[pos_x][pos_y] == '-1'，否则遇到水也会继续扩散。
            if grid[pos_x][pos_y] != '1':
                return
            grid[pos_x][pos_y] = '-1'
            mark_neighbor_land(grid, pos_x + 1, pos_y)
            mark_neighbor_land(grid, pos_x - 1, pos_y)
            mark_neighbor_land(grid, pos_x, pos_y + 1)
            mark_neighbor_land(grid, pos_x, pos_y - 1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    mark_neighbor_land(grid, x, y)
                    ans += 1

        return ans

