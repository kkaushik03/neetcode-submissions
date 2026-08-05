class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        stack = deque()
        visited = []
        neighbors = [(-1,0),(1,0),(0,1),(0,-1)]
          

        for col in range (cols):
            if board[0][col] == 'O':
                board[0][col]='#'
                stack.append((0,col))
                
            if board[rows-1][col]=='O':
                board[rows-1][col]='#'
                stack.append((rows-1,col))
                
        for row in range (rows):
            if board[row][cols-1]=='O':
                board[row][cols-1]='#'
                stack.append((row,cols-1))
                
            if board[row][0]=='O':
                board[row][0]='#'
                stack.append((row,0))
                
                
        while stack:
            r,c = stack.pop()
            visited.append(board[r][c])
            for ar,ac in neighbors:
                nr , nc = ar+r,ac+c
                
                if( 0 <= nr < rows and 0 <= nc < cols and board[nr][nc]=='O'):
                    board[nr][nc]='#'
                    stack.append((nr,nc))
                    

        for col in range (cols):
            for row in range (rows): 
                if(board[row][col]=='O'):
                    board[row][col]='X'
                if(board[row][col]=='#'):
                    board[row][col]='O'


            

        