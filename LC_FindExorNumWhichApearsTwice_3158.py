class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res=0
        s=set()
        for i in range(len(nums)):
            if nums.count(nums[i])==2 and nums[i] not in s:
                res^=nums[i]
                s.add(nums[i])

        return res
        
