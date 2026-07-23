class Solution:
    def digitCount(self, num: str) -> bool:
        res=True
        for i in range(len(num)):
            if num.count(str(i))!=int(num[i]):
                res=False
        return res
