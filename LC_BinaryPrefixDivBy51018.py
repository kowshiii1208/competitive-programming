class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[False]*len(nums)
        s="".join(map(str,nums))
        for i in range(len(nums)):
            if int(s[:i+1],2)%5==0:
                res[i]=True
        return res
