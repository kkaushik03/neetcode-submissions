class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> set():
        rows=len(heights)
        cols=len(heights[0])

        def dfs(heights,p) -> List[(int,int)]:
                stack=deque()
                visited=set()
                neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
                if p=="p":
                    for j in range(cols):        # top row
                        stack.append((0, j))
                    for k in range(rows):        # left col
                        stack.append((k, 0))
                if p=="a":
                    for j in range(cols):        # last row: every column
                        stack.append((rows-1, j))
                    for k in range(rows):        # last col: every row
                        stack.append((k, cols-1))

                while(stack):
                    r,c = stack.pop()            
                    if (r,c) in visited:
                        continue
                    else:
                        visited.add((r,c))
                    for ar,ac in neighbors:
                        dr,dc = r+ar, ac+c   # 
                        if(dr>=0 and dc>=0 and dr<rows and dc<cols and (dr,dc) not in visited and heights[dr][dc]>=heights[r][c]):
                            stack.append((dr,dc)) 
                return visited         

        atlantic = dfs(heights,"a")
        pacific = dfs(heights,"p")
        return [[r, c] for r, c in (pacific & atlantic)]
        
         
        
        
        
        

                        
                    


        