class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ma,md = 0,0
        for l,w in dimensions:
            cd = l*l + w*w
            if cd>md or(cd== md and l*w>ma):
                md = cd
                ma = l*w
        return ma