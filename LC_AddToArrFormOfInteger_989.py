class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res=0
        for i in num:
            res=res*10+i
        res=res+k
        r=[]
        while res>0:
            r.append(res%10)
            res//=10
        return r[::-1]
            
