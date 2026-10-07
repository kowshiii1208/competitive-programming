class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        m=1<<n
        res=[]
        for i in range(m):
            sub=[]
            for j in range(n):
                if i&(1<<j)!=0:
                    sub.append(nums[j])
            res.append(sub)
        return res