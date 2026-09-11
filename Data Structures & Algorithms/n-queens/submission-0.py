class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=[['.' for i in range(n)] for j in range(n)]
        cols=set()
        diagMinus=set()
        diagPlus=set()
        def backtrack(row):
            if row==n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row-col) in diagMinus or (row+col) in diagPlus:
                    continue
                cols.add(col)
                diagMinus.add(row-col)
                diagPlus.add(row+col)
                board[row][col]='Q'
                backtrack(row+1)
                cols.remove(col)
                diagMinus.remove(row-col)
                diagPlus.remove(row+col)
                board[row][col]='.'
        backtrack(0)
        return res