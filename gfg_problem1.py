class Solution:
    def countTriplets(self, arr, target):
        # code here
        n=len(arr)
        arr.sort()
        res=0
        
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                s=arr[i]+arr[l]+arr[r]
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    el1=arr[l]
                    el2=arr[r]
                    c1=0
                    c2=0
                    while l<=r and el1==arr[l]:
                        l+=1
                        c1+=1
                    while l<=r and el2==arr[r]:
                        r-=1
                        c2+=1
                    if el1==el2:
                        res+= (c1*(c1-1))//2
                    else:
                        res+=(c1*c2)
        return res
                    
            
