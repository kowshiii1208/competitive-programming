class Solution:
    def missingNumber(self, arr):
        # code here
        res=1
        arr.sort()
        for i in range(len(arr)):
            if res == arr[i]:
                res+=1
            elif arr[i]>res:
                break
        return res
