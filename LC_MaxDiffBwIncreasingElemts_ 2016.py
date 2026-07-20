class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res=0
        if nums==sorted(nums,reverse=True):
            return -1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i<j and nums[i]<nums[j]:
                    res=max(res,nums[j]-nums[i])
        return res
