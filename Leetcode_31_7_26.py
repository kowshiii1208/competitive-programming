class Solution:
    def minimumPushes(self, word: str) -> int:
        freq={}
        res=0
        for ch in word:
            freq[ch]=freq.get(ch,0)+1
        li=sorted(freq.values(),reverse=True)
        for i in range(len(li)):
            if i<8:
                res+=li[i]
            elif i<16:
                res+=(li[i]*2)
            elif i<24:
                res+=(li[i]*3)
            elif i>=24:
                res+=(li[i]*4)
        return res
       
