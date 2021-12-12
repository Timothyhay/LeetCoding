class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, col, row):
            if len(word) == 0:
                return True
            if col < 0 or col >= len(board[0]) or row < 0 or row >= len(board) or word[0] != board[row][col]:
                return False

            temp = board[row][col]
            board[row][col] = '#'

            res = dfs(board, word[1:], col + 1, row) \
                  or dfs(board, word[1:], col - 1, row) \
                  or dfs(board, word[1:], col, row + 1) \
                  or dfs(board, word[1:], col, row - 1)

            # Need to recover the visited sign for another search
            board[row][col] = temp
            return res

        for row in range(len(board)):
            for col in range(len(board[0])):
                # newboard = board
                if dfs(board, word, col, row):
                    return True

        return False