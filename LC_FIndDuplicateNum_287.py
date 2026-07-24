class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=set()
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                res=nums[i]
                break
        return res
