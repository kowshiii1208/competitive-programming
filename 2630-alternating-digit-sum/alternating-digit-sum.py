class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = 0
        digits = [int(i) for i in str(n)]
        for i in range(len(digits)):
            if i%2==0:
                s+=digits[i]
            else:
                s-=digits[i]
        return s