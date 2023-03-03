
class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        ##Your code here
        val=bin(N)
        mx=0
        cnt=0
        for i in range(2,len(val)):
            if val[i]=="1":
                cnt+=1
            else:
                mx=max(cnt,mx)
                cnt=0
        
        return max(cnt,mx)
