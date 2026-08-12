class Solution:
    def rob(self, nums: List[int]) -> int:
        


        def helper(nums,start,end):
            n = end-start + 1 
            if n==0: 
                return nums[0]
            if n==1:
                return nums[start]
            if n==2:
                return max(nums[start],nums[end])

            dp = [-1] * n
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start+1])
            for i in range (2, n):
                dp[i]= max(dp[i-1],dp[i-2]+nums[start+i])
            return dp[n-1]
        return max(helper(nums,0,len(nums)-2),helper(nums,1,len(nums)-1))



    

        

