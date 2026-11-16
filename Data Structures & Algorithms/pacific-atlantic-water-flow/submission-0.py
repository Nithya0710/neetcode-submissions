from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols=len(heights), len(heights[0])
        directions=[(0,1), (1,0), (0,-1), (-1,0)]
        pac=[[False]*cols for _ in range(rows)]
        atl=[[False]*cols for _ in range(rows)]

        def bfs(src, ocean):
            queue=deque(src)
            while queue:
                r, c=queue.popleft()
                ocean[r][c]=True
                for dr, dc in directions:
                    nr, nc=r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and not ocean[nr][nc] and heights[nr][nc]>=heights[r][c]:
                        queue.append((nr, nc))

        pacific, atlantic=[], []
        for c in range(cols):
            pacific.append((0,c))
            atlantic.append((rows-1,c))
        for r in range(rows):
            pacific.append((r,0))
            atlantic.append((r,cols-1))
        bfs(pacific, pac)
        bfs(atlantic, atl)
        res=[]
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        return res