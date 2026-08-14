class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)+1
        n = len(text2)+1
        dp = [[-1] * n for _ in range(m)]
        m = len(text1)
        n = len(text2)
        for row1 in range (m+1): 
            for col1 in range (n+1): 
                if row1 == 0 or col1 ==0:
                    dp[row1][col1]=0
        for row in range (1,len(text1)+1):
            for col in range (1,len(text2)+1): 
                if text1[row-1] == text2[col-1]: 
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        return dp[m][n]