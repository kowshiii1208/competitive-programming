class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s==0:
            return 0
        elif s>9*n:
            return -1
        res=[0]*n
        for i in range(n):
            res[i]=min(9,s)
            s-=min(9,s)
        return int("".join(map(str,res)))
