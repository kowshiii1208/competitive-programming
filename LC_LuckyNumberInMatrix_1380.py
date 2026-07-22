class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        min_l=[]
        max_l=[]
        for i in range(m):
            mi=float('inf')
            for j in range(n):
                mi=min(mi,matrix[i][j])
            min_l.append(mi)
        for i in range(n):
            mx=float('-inf')
            for j in range(m):
                mx=max(mx,matrix[j][i])
            max_l.append(mx)
        res=[]
        for i in min_l:
            if i in max_l:
                res.append(i)
        return res
