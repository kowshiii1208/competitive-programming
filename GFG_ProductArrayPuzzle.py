class Solution:
    def productExceptSelf(self, arr):
        # code here
        z=0
        n=len(arr)
        res=[0]*n
        p=1
        idx=-1
        for i in range(n):
            if arr[i]==0:
                z+=1
                idx=i
            else:
                p*=arr[i]
        if z==0:
            for i in range(n):
                res[i]=p//arr[i]
        elif z==1:
            res[idx]=p
        return res
        
