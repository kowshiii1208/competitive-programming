class Solution:
    def largestInteger(self, num: int) -> int:
        l=[int(d) for d in str(num)]
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i]%2==0 and l[j]%2==0 :
                    if l[i]<l[j] and i<j:
                        l[i],l[j]=l[j],l[i]
                elif l[i]%2==1 and l[j]%2==1:
                    if l[i]<l[j] and i<j:
                        l[i],l[j]=l[j],l[i]
        return int("".join(map(str, l)))




        
