'''
    DFS
    Matrix

    # Remember to save the original status for other attempts
    temp = board[r][c]
    board[r][c] = "#"
    res = dfs(r + 1, c, board, i + 1) or dfs(r, c + 1, board, i + 1) \
            or dfs(r - 1, c, board, i + 1) or dfs(r, c - 1, board, i + 1)
    board[r][c] = temp

'''
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        def dfs(r, c, board, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r == len(board) or c == len(board[0]) or word[i] != board[r][c]:
                return False

            # Remember to save the original status for other attempts
            temp = board[r][c]
            board[r][c] = "#"
            res = dfs(r + 1, c, board, i + 1) or dfs(r, c + 1, board, i + 1) \
                  or dfs(r - 1, c, board, i + 1) or dfs(r, c - 1, board, i + 1)
            board[r][c] = temp

            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, board, 0):
                    return True
        return False


exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")