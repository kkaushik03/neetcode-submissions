class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = [] 

        n = len(candidates)
        candidates.sort()  # Sort to handle duplicates
        def helper(combo,remainder,start):
            if remainder==0: 
                result.append(combo[:])
                return 
            if remainder<0:
                return 
            #there is some value left: 
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                
                combo.append(candidates[i])
                helper(combo,remainder-candidates[i],i+1)
                combo.pop()
            
        helper([],target,0)
        return result
