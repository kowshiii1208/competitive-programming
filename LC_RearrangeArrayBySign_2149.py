class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr=[]
        e=0
        o=1
        for i in range(len(nums)):
            if nums[i]>0:
                arr.insert(e,nums[i])
                e+=2
            else:
                arr.insert(o,nums[i])
                o+=2
        return arr
            
