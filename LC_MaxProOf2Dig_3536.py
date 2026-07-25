class Solution:
    def maxProduct(self, n: int) -> int:
        li=[int(d) for d in str(n)]
        li=sorted(li,reverse=True)
        return li[0]*li[1]
