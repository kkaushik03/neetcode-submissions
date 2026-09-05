class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        memo = {}  # (index, remaining) -> bool
        
        def canPart(index, remaining):
            if remaining == 0:
                return True
            if index >= len(nums) or remaining < 0:
                return False
            
            if (index, remaining) in memo:
                return memo[(index, remaining)]
            
            # Include nums[index]
            p1 = canPart(index + 1, remaining - nums[index])
            # Exclude nums[index]
            p2 = canPart(index + 1, remaining)
            
            memo[(index, remaining)] = p1 or p2
            return memo[(index, remaining)]
        
        return canPart(0, target)