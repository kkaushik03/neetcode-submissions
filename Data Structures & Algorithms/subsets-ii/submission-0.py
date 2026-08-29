class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []


        nums.sort()
        def helper(combo,start):
            result.append(combo[:]) 
            for i in range(start,len(nums)): 
                if i > start and nums[i]==nums[i-1]:
                    continue
                combo.append(nums[i])
                helper(combo,i+1)
                combo.pop()
        helper([],0)
        return result