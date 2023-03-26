class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        s=str(N)
        return pow(int(s),int(s[::-1]),1000000007)
