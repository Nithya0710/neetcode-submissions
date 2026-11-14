from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid), len(grid[0])
        queue=deque()
        fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    queue.append((r,c))
        directions=[(0,1), (1,0), (0,-1), (-1,0)]
        mins=0
        while queue:
            size=len(queue)
            rotten=False
            for _ in range(size):
                r, c=queue.popleft()
                for dr, dc in directions:
                    nr, nc=r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        rotten=True 
                        grid[nr][nc]=2
                        fresh-=1
                        queue.append((nr,nc))
            if rotten:
                mins+=1
        if fresh>0:
            return -1
        return mins                    