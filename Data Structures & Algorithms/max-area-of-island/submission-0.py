class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        best = 0 
        def area(row,col):
            if(row<0 or row>=rows or col<0 or col>=cols or grid[row][col]==0):
                return 0
            grid[row][col]=0
            return 1 + area(row+1,col) + area(row-1,col) + area(row,col+1) + area(row,col-1)
        for r in range(rows):
            for c in range(cols):
                best= max(best,area(r,c))
        return best 







    

        