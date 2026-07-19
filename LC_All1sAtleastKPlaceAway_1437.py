class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dif=0
        l=[]
        for i in range(len(nums)):
            if nums[i]==1:
                l.append(i+1)
        for i in range(len(l)-1):
            if abs(l[i]-l[i+1])-1<k:
                return False
        return True
