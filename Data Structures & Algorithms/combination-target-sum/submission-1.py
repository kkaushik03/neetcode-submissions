class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]

        def helper(combo,remaining,start):
            if remaining==0:
                result.append(combo[:])
                return 
            if remaining<0:
                return 
            #if the remaining is still left: 
            for i in range (start,len(nums)):
                combo.append(nums[i])
                helper(combo,remaining-nums[i],i)
                combo.pop()
        helper([],target,0)
        return result


