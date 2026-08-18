class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices) + 2)]
        def helper(currentday,bagfull):
            if currentday<len(prices):
                #here the currentday is in the prices range 
                
                if (bagfull==1):
                    if dp[currentday][1]!=0:
                        return dp[currentday][1]
                    else:
                        dp[currentday][1]= max(prices[currentday]+helper(currentday+2,0),helper(currentday+1,1))
                        return dp[currentday][1]
                else: 
                    if dp[currentday][0]!=0:
                        return dp[currentday][0]
                    else:
                        dp[currentday][0]= max(helper(currentday+1,0),-prices[currentday]+helper(currentday+1,1))
                        return dp[currentday][0] 
            return 0
        
        return helper(0,0)