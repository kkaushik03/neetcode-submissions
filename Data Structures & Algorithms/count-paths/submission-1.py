class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        self.result = 0 
        def solvePath(i,j)->int:
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            
            if i==m-1 and j==n-1:
                self.result=self.result+1
                return 1
            if dp[i][j]!=-1:
                return dp[i][j] 
            dp[i][j]=solvePath(i+1,j)+solvePath(i,j+1)
            return dp[i][j]

        extra = solvePath(0,0)
        return extra