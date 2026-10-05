class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        ans = 0
        for i in s:
            if i == '(':
                st.append(ans)
                ans = 0
            else:
                ans = st[len(st)-1]+max(2*ans,1)
                st.pop()
        return ans
