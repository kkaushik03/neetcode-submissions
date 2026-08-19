class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = amount 
        n = len(coins)
        dp = [[-1]*(amount+1) for i in range (0,n+1)]

        def solve(amountleft, index): 
            if amountleft==0:
                return 1
            if index>=n:
                return 0
            if dp[index][amountleft]!=-1:
                return dp[index][amountleft]
            if coins[index]>amountleft: 
                dp[index][amountleft]=solve(amountleft,index+1)
            else:
                dp[index][amountleft]= solve(amountleft,index+1)+solve(amountleft-coins[index],index)
            return dp[index][amountleft]


        return solve(amount,0)