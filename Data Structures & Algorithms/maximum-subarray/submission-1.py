class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = current = nums[0]
        for num in nums[1:]:  # Start from index 1
            current = max(num, num + current)
            best = max(current, best)
        return best