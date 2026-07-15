
class Solution:
    def maxLength(self, s):
        # code here
        st=[]
        st.append(-1)
        ml=0
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ml=max(ml,i-st[-1])
        return ml
