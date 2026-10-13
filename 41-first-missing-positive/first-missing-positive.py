class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res=1
        nums.sort()
        for i in nums:
            if i==res:
                res+=1
            elif i>res:
                break
        return res