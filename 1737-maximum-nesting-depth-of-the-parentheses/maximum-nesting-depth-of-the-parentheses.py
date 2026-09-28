class Solution:
    def maxDepth(self, s: str) -> int:
        dep = 0
        res = 0
        for i in s:
            if i == '(':
                dep+=1
                res = max(res,dep)
            elif i == ')':
                dep-=1
            else:
                continue
        return res
