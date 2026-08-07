t=int(input())
while t>0:
    t-=1
    a,b,c=map(int,input().split())
    cn=0
    while(a!=b and a!=c and b!=c):
        if a>b and a>c:
            a-=1
        elif b>c:
            b-=1
        else:
            c-=1
        if a<b and a<c:
            a+=1
        elif b<c:
            b+=1
        else:
            c+=1
        cn+=1
    print(cn)
