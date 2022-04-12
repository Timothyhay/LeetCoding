'''
    Array 1
    Always travers from top right to bottom left, reverse intermediate result when i % 2 == 0
'''

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        intermed = []
        m = len(mat)
        n = len(mat[0])
        for i in range(m + n):
            intermed.clear()
            row = 0
            col = i
            if i >= n:
                row = i - n + 1
                col = n - 1
            while row < m and col >= 0:
                intermed.append(mat[row][col])
                row += 1
                col -= 1

            if i % 2 == 0:
                ans.extend(intermed[::-1])
            else:
                ans.extend(intermed)

        return ans


