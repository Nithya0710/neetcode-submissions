class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        rows, cols=len(board), len(board[0])

        def backtrack(r, c, i):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or board[r][c]!=word[i]:
                return False
            if i==len(word)-1:
                return True
            visited.add((r,c))
            up=backtrack(r+1,c,i+1)
            down=backtrack(r-1,c,i+1)
            left=backtrack(r,c-1,i+1)
            right=backtrack(r,c+1,i+1)
            if up or down or left or right:
                return True
            else:
                visited.remove((r,c))
                return False
        
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        return False