class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []


        def helper(presentstr,numopen,numclose):
            if len(presentstr)==n*2: 
                result.append(presentstr)
                return 

            if(numopen<n):
                presentstr=presentstr+"("
                helper(presentstr,numopen+1,numclose)
                presentstr=presentstr[:-1]
            if numclose<numopen:
                presentstr=presentstr+")"
                helper(presentstr,numopen,numclose+1)
                presentstr=presentstr[:-1]
        helper("",0,0)
        return result 