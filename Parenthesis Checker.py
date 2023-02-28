class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        stack=[]
        for i in x:
            if stack and stack[-1]=="[" and i=="]":
                stack.pop()
            elif stack and stack[-1]=="{" and i=="}":
                stack.pop()
            elif stack and stack[-1]=="(" and i==")":
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==0
