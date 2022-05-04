'''
    DFS

    for every cell, start a DFS.
    maintain a visited matrix
    for DFS func, DFS for 4 directions.
    Do a recursive DFS after checking isSafe (within boundary and c == crtChar and not visited)
'''

maxRow = 500
maxCol = 500

visited = [[0 for _ in range(maxCol)] for _ in range(maxRow)]

# Function for depth first search
def DFS(M, row, col, c, R, C):
    # These arrays are used to get row
    # and column numbers of 4 neighbours
    # of a given cell
    rowVec = [-1, 1, 0, 0]
    colVec = [0, 0, -1, 1]
    visited[row][col] = True

    # Recur for all connected neighbours
    for k in range(4):
        # Before DFS, check isSafe First
        if row + rowVec[k] >= 0 and row + rowVec[k] < R and \
                col + colVec[k] >= 0 and col + colVec[k] < C and \
                M[row + rowVec[k]][col + colVec[k]] == c and \
                not visited[row + rowVec[k]][col + colVec[k]]:
            DFS(M, row + rowVec[k], col + colVec[k], c, R, C)


# Function to return the number of
# connectewd components in the matrix
def connectedComponents(M, n):
    connectedComp = 0
    R = len(M)
    C = len(M[0])

    for i in range(R):
        for j in range(C):
            if (not visited[i][j]):
                c = M[i][j]
                DFS(M, i, j, c, R, C)
                connectedComp += 1

    return connectedComp

'''
# Function that return true if mat[row][col]
# is valid and hasn't been visited
def isSafe(M, row, col, c, n, l):
    # If row and column are valid and element
    # is matched and hasn't been visited then
    # the cell is safe
    return ((row >= 0 and row < n) and
            (col >= 0 and col < l) and
            (M[row][col] == c and not
            visited[row][col]))
'''

# Driver code
if __name__ == "__main__":
    M = ["aabba",
         "aabba",
         "aaaca"]
    n = len(M)

    print(connectedComponents(M, n))
