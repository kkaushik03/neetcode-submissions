class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        combo=[]

        def helper():
            if len(combo)==len(nums):
                result.append(combo[:])
                return
            for num in nums:
                if not num in combo:
                    combo.append(num)
                    helper()
                    combo.pop()
        helper()
        return result