class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)




        def helper(index,current): 
            if index==n:
                result.append(current[:])
                return
            # adding the number
            current.append(nums[index])
            helper(index+1,current)
            # not adding the number
            current.pop()
            helper(index+1,current)
        helper(0,[])
        return result
