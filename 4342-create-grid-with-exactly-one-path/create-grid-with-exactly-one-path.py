class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        if m==1:
            return ["."*n]
        if n==1:
            return ["."]*m
        grid.append("."*n)
        for i in range(m-1):
            grid.append("#"*(n-1)+".")
        return grid