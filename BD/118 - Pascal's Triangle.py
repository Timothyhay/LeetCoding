# 118. Pascal's Triangle
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return pascal
        layer = 2
        while len(pascal) < numRows:
            crtRow = [1]
            for i in range(1, layer):
                crtRow.append(pascal[layer-1][i-1] + pascal[layer-1][i])
            crtRow.append(1)
            pascal.append(crtRow)
            layer += 1
        return pascal

'''
def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
explanation: Any row can be constructed using the offset sum of the previous row. Example:

    1 3 3 1 0 
 +  0 1 3 3 1
 =  1 4 6 4 1
 
Ref: https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.
'''

if __name__ == '__main__':
    s = Solution()
    s.generate(5)
