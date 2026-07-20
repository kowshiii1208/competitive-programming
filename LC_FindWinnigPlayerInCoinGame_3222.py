class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        res=0
        n=x
        for i in range(n):
            if x>=1 and y>=4:
                x-=1
                y-=4
                res+=1
        if res%2==1:
            return "Alice"
        return "Bob"
