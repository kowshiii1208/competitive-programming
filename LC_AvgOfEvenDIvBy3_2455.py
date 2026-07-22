class Solution:
    def averageValue(self, nums: List[int]) -> int:
        c=s=0
        for i in range(len(nums)):
            if nums[i]%6==0:
                c+=1
                s+=nums[i]
        if c==0:
            return 0
        return s//c
        
