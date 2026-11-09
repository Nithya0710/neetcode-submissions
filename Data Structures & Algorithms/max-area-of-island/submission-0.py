from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols=len(grid), len(grid[0])
        directions=[(0,1), (1,0), (0,-1), (-1,0)]

        def bfs(row, col):
            queue=deque()
            grid[row][col]=0
            queue.append((row,col))
            res=1
            while queue:
                r, c=queue.popleft()
                for dr, dc in directions:
                    nr, nc=r+dr, c+dc
                    if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]==0:
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc]=0
                    res+=1
            return res
        
        area=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    area=max(area, bfs(row, col))
        return area