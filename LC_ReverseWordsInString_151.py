class Solution:
    def reverseWords(self, s: str) -> str:
        li=s.split()
        res=[]
        for word in range(len(li)-1,-1,-1):
            res.append(li[word])
        return " ".join(res)
            
        
