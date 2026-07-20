class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        if len(res)==1:
            res.append(res[0])
        if res:
            return [res[0],res[-1]]
        return [-1,-1]
