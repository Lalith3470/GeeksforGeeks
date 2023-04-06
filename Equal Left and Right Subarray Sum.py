
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equalSum(self,A, N):
        # Your code here
        sm=sum(A)
        st=0
        for i in range(len(A)):
            sm-=A[i]
            if st==sm:return i+1
            st+=A[i]
        return -1
