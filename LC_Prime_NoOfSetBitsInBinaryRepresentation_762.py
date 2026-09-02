def sieve(n):
    num = (10**6)+1
    prime = [True]*num
    prime[0]=prime[1]=False
    p = 2
    while p*p < num:
        if prime[p]:
            for j in range(p*p,num,p):
                prime[j] = False
        p+=1
    return prime
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = sieve(right)
        c=0
        for i in range(left,right+1):
            if prime[bin(i)[2:].count('1')]:
                c+=1
        return c
