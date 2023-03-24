class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        c=0
        for i in range(N):
            if A[i]<=X:
                c+=1
            else:break
        if c>0:return c-1 
        return -1
