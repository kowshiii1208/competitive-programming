class Solution:
    def maxLen(self, arr):
        # code here
        mp={}
        ps=0
        res=0
        for i in range(len(arr)):
            ps+=-1 if arr[i]==0 else 1
            if ps==0:
                res=i+1
                
                
            elif ps in mp:
                res=max(res,i-mp[ps])
            else:
                mp[ps]=i
        return res
        
