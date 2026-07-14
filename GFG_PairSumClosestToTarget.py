class Solution:
    def sumClosest(self, arr, target):
        # code here
        n=len(arr)
        l=0
        r=n-1
        res=[]
        arr.sort()
        md=float('inf')
        while l<r:
            s=arr[l]+arr[r]
            if abs(s-target)<md:
                md=abs(s-target)
                res=[arr[l],arr[r]]
            elif abs(s-target)==md:
                if (arr[r]-arr[l])>(res[1]-res[0]):
                    res=[arr[l],arr[r]]
            if s<target:
                l+=1
            elif s>target:
                r-=1
            else:
                break
        return res
