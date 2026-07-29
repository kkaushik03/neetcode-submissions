class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
        for r in range (rows):
            for c in range (cols): 
                if(grid[r][c]==0):
                    q.append((r, c))
        neighbors = [(1,0),(-1,0),(0,-1),(0,1)]

        while q: 
            r,c = q.popleft()
            for dr, dc in neighbors:
                nr,nc=r+dr,c+dc
                if 0<=nr and rows>nr and nc>=0 and cols>nc and grid[nr][nc]==INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
