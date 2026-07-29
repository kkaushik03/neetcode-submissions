class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        time = 0
        fresh = 0 
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        cols = len(grid[0])
        for row in range (rows):
            for col in range (cols):
                if(grid[row][col]==2):
                    queue.append((row,col))
                elif(grid[row][col]==1):
                    fresh = fresh + 1 
        while queue and fresh>0: 
            for _ in range (len(queue)):
                r,c = queue.popleft()       
                grid[r][c]=0
                for r_,c_ in neighbors:
                    nr,nc=r+r_,c+c_
                    if(nr<rows and nc < cols and nc>=0 and nr>=0 and grid[nr][nc] == 1):
                                grid[nr][nc]=2
                                fresh = fresh-1
                                queue.append((nr,nc))
            time=time+1     
        if fresh == 0:
            return time
        return -1            

            


                