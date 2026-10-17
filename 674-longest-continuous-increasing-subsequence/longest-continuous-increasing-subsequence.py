class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        res = 0
        count = 0
        if len(nums)<=1:
            return 1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count+=1
            else:
                count = 0
            res = max(count+1,res)
        return res

