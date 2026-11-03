class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols=len(grid), len(grid[0])
        visited=set()
        directions=[(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(r, c):
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc=r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc]=='1':
                    dfs(nr, nc)

        islands=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1' and (row,col) not in visited:
                    islands+=1
                    dfs(row, col)
        return islands