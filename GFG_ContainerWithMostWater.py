class Solution:
    def maxWater(self, arr):
        # code here
        l=0
        r=len(arr)-1
        mx=0
        while l<r:
            area=min(arr[l],arr[r])*(r-l)
            mx=max(mx,area)
            if arr[l]<arr[r]:
                l+=1
            else:
                r-=1
        return mx
            
