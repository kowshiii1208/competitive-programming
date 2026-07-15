import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        es=0
        os=0
        for i in range(1,(2*n)+1):
            if i%2==0:
                es+=i
            else:
                os+=i
        return math.gcd(os,es)
