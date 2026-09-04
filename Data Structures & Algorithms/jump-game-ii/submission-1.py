class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo={}
        def helper(index):
            if index>=len(nums)-1:
                return 0
            if index in memo:
                return memo[index]
            if nums[index]==0:
                return float('inf')
            
            min_jump = float('inf')

            
            for jump in range(1,nums[index]+1):
                next_jump = index+jump
                jumps = helper(next_jump)
                min_jump = min(min_jump,1+jumps)

            memo[index]=min_jump
            return min_jump
        return helper(0)
            
