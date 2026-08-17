class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)+1
        n = len(text2)+1
        dp = [[0] * n for _ in range(m)]
            
        for p in range (1,m):
            for q in range (1,n):
                if text1[p-1]==text2[q-1]:
                    dp[p][q]=dp[p-1][q-1]+1
                else:
                    dp[p][q]=max(dp[p-1][q],dp[p][q-1])
        return dp[m-1][n-1]