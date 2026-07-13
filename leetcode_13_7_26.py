class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nw=[]
        r="123456789"
        l=len(str(low))
        h=len(str(high))
        for i in range(l,h+1):
            for st in range(10-i):
                num=int(r[st:st+i])
                if low<=num<=high:
                    nw.append(num)
        return nw
