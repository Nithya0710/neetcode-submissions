from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols=len(board), len(board[0])
        directions=[(0,1), (1,0), (0,-1), (-1,0)]

        def bfs():
            queue=deque()
            for r in range(rows):
                for c in range(cols):
                    if (r==0 or r==rows-1 or c==0 or c==cols-1) and board[r][c]=='O':
                        queue.append((r,c))
            while queue:
                r, c=queue.popleft()
                if board[r][c]=='O':
                    board[r][c]='T'
                    for dr, dc in directions:
                        nr, nc=r+dr, c+dc
                        if 0<=nr<rows and 0<=nc<cols:
                            queue.append((nr, nc))
            
        bfs()
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='T':
                    board[r][c]='O'