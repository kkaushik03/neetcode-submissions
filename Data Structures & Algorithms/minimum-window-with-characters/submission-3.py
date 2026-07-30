class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        def is_valid():
            for k in need:
                if have.get(k, 0) < need[k]:
                    return False
            return True

        need = {}
        have = {}
        left = 0
        right = 0
        resultsubstr=""
        for ch in t:
            if ch not in need:
                need[ch]=1
            else:
                need[ch]=need[ch]+1

        for char in s: 
            if char in need:
                if char not in have:
                    have[char] = 1
                else:
                    have[char] = have.get(char, 0) + 1
                while is_valid():
                    tempres = s[left:right+1]
                    if(resultsubstr == "" or len(tempres) < len(resultsubstr)):
                            resultsubstr=tempres
                    if( s[left] in need):
                        have[s[left]]=have[s[left]]-1
                    left=left+1
            right=right+1
        return resultsubstr