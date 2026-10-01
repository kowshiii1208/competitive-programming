class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if stack and ((stack[-1]=='(' and i==')') or
                             (stack[-1]=='{' and i=='}') or 
                             (stack[-1]=='[' and i==']')):
                             stack.pop()
                else:
                    return False
        if stack:

            return False
        return True
            