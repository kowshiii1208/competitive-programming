class Solution:
    def maxPower(self, s: str) -> int:
        li=[]
        l = 0
        res = 0
        if len(s)==1:
            return 1
        for i in range(len(s)-1):
            if ord(s[i])-ord(s[i+1])==0:
                l+=1
            else:
                l = 0
            res = max(res,l+1)
        return res

