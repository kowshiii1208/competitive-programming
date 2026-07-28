class Solution:
    def reverseByType(self, s: str) -> str:
        al=[]
        sp=[]
        res=[]
        for i in s:
            if i.isalpha():
                al.append(i)
            else:
                sp.append(i)
        al=al[::-1]
        a1=0
        sp=sp[::-1]
        s1=0
        for i in s:
            if i.isalpha():
                res.append(al[a1])
                a1+=1
            else:
                res.append(sp[s1])
                s1+=1
        return "".join(map(str,res))
