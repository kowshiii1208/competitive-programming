class Solution:
    def isBalanced(self, s):
        # code here
        st=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                st.append(i)
            else:
                if st and ((st[-1]=='(' and i==')') or
                           (st[-1]=='[' and i==']') or
                           (st[-1]=='{' and i=='}')):
                               st.pop()
                else:
                    return False
        if st:
            return False
        return True
