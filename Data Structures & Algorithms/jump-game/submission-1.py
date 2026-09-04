class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # Farthest index we can reach
        
        for i in range(len(nums)):
            if i > max_reach:  # Current index is unreachable
                return False
            max_reach = max(max_reach, i + nums[i])  # Update farthest reach
            if max_reach >= len(nums) - 1:  # Can reach the end
                return True
        
        return False