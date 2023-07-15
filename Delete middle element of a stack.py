#User function Template for python3
import math
class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here
        n=((sizeOfStack+1)//2)-1
        for i in range(n,sizeOfStack-1):
            s[i]=s[i+1]
        s.pop()
