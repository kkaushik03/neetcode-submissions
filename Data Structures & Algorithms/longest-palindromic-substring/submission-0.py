class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.bestleft = 0
        self.bestright = 0
        n = len(s)
        def expand(left,right): 
            while left>=0 and right<n and s[left]==s[right]:
                left=left-1
                right=right+1
            left=left+1
            right=right-1
            if right-left > self.bestright-self.bestleft:
                self.bestright=right
                self.bestleft=left
            
        

            #goal here is to find the bestright and best left
        for center in range (n):
                expand(center,center+1)
                expand(center,center)
        return s[self.bestleft:self.bestright+1]
