class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        m = 2*sum(nums)+1
        dp = [[-1]*(m) for i in range (n+1)]
        def helper(index,pval):

            if index >= n:
                if pval==target: 
                    return 1
                if pval!=target: 
                    return 0
            offset_pval = pval + sum(nums)
            if dp[index][offset_pval]!=-1:
                return dp[index][offset_pval]
            add = helper(index+1,pval+nums[index])
            sub = helper(index+1,pval-nums[index])
            dp[index][offset_pval]=add+sub
            return dp[index][offset_pval]
        return helper(0,0)