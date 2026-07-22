class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z=0
        idx=-1
        p=1
        res=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                z+=1
                idx=i
            else:
                p*=nums[i]
        if z==0:
            for i in range(len(nums)):
                res[i]=p//nums[i]
        elif z==1:
            res[idx]=p
        return res
        
