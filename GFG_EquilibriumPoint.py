class Solution:
    def findEquilibrium(self, arr):
        # code here
        n=len(arr)
        t=sum(arr)
        l=0
        for i in range(n):
            t-=arr[i]
            if t==l:
                return i
            l+=arr[i]
        return -1

