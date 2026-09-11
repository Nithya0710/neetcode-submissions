from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares=defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=='.':
                    continue
                val=board[r][c]
                if val in rows[r] or val in cols[c] or val in squares[(r//3, c//3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[(r//3, c//3)].add(val)
        return True