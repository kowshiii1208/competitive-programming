class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        s=list(set(nums))
        for i in range(len(s)):
            if nums.count(s[i])==1:
                res=s[i]
                break
        return res
