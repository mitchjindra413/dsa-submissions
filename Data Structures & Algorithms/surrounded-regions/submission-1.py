class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for r in range(len(board)):
            if r == 0 or r == len(board) - 1:
                for c in range(len(board[r])):
                    if board[r][c] == "O":
                        self.mark(r, c, board)
            else:
                for c in [0, len(board[r]) - 1]:
                    if board[r][c] == "O":
                        self.mark(r, c, board)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

    def mark(self, r: int, c: int, board: List[List[str]]) -> None:
        if r < 0 or r >= len(board):
            return
        if c < 0 or c >= len(board[r]):
            return
        if board[r][c] != "O":
            return

        board[r][c] = "S"
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dr, dc in directions:
            self.mark(dr + r, dc + c, board)
