'''
    Dynamic Programming
    Matrix

    Time Complexity: O(M×N). The rectangular grid given to us is of size M×N and we process each cell just once.
    Space Complexity: O(1). We are utilizing the obstacleGrid as the DP array. Hence, no extra space.
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
            return 0

        R = len(obstacleGrid)
        C = len(obstacleGrid[0])

        obstacleGrid[0][0] = 1
        for i in range(1, R):
            # If last row 'has a path' and this row 'is not a obstacle'
            if obstacleGrid[i - 1][0] == 1 and obstacleGrid[i][0] == 0:
                # Mark it 'has a path'
                obstacleGrid[i][0] = 1
            else:
                # Since the Col 0 has only 1 dir to enter, else we mark it 'has no path'
                obstacleGrid[i][0] = 0

        for i in range(1, C):
            if obstacleGrid[0][i - 1] == 1 and obstacleGrid[0][i] == 0:
                obstacleGrid[0][i] = 1
            else:
                obstacleGrid[0][i] = 0

        for r in range(1, R):
            for c in range(1, C):
                # Starting from cell(1,1) fill up the values
                # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
                # i.e. From above and left.
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]

        return obstacleGrid[-1][-1]
