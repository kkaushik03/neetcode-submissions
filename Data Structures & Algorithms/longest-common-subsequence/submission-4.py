class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)+1
        n = len(text2)+1
        dp = [[-1] * n for _ in range(m)]
        def helper(text1,text2,text1_m,text2_n):
            if text1_m == 0 or text2_n ==0: 
                return 0
            elif dp[text1_m][text2_n] != -1: 
                return dp[text1_m][text2_n]
            else:
                if text1[text1_m-1] == text2[text2_n-1]: 
                    dp[text1_m][text2_n] = 1+helper(text1,text2,text1_m-1, text2_n-1)
                    return dp[text1_m][text2_n]
                else:
                    dp[text1_m][text2_n] = max(helper(text1,text2,text1_m-1,text2_n), helper(text1,text2,text1_m, text2_n-1))
                    return dp[text1_m][text2_n]
            
        return helper(text1,text2,len(text1),len(text2))
         