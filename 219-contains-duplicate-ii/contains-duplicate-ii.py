class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res=False
        fre={}
        for i in range(len(nums)-1,-1,-1):
            if nums[i] not in fre.keys():
                fre[nums[i]]=i
            else:
                if abs(fre[nums[i]]-i)<=k:
                    return True
                else:
                    fre[nums[i]]= i
        return False
