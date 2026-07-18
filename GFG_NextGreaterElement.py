class Solution:
    def nextLargerElement(self, arr):
        # code here
        n=len(arr)
        res=[-1]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and arr[st[-1]]<=arr[i]:
                st.pop()
            if st:
                res[i]=arr[st[-1]]
            st.append(i)
        return res
