class Solution:
    def isThree(self, n: int) -> bool:
        div=2
        if n<=3:
            return False
        for i in range(2,(n//2)+1):
            if n%i==0:
                div+=1
        return div==3

            
