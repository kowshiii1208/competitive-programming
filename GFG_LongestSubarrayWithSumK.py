class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        res=0
        ps=0
        m={}
        for i in range(len(arr)):
            ps+=arr[i]
            if ps==k:
                res=i+1
            elif ( ps-k) in m:
                res=max(res,i-m[ps-k])
            if ps not in m:
                m[ps]=i
        return res
            
