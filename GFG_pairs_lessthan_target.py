class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        pair=0
        arr.sort()
        r=len(arr)-1
        l=0
        while l<r:
            s=arr[l]+arr[r]
            if s>=target:
                r-=1
            else:
                pair+=(r-l)
                l+=1
            
        return pair
