#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        
        # code here
        dp=[[0]*(y+1) for i in range(x+1)]
        mx=0
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            mx=max(dp[i][j],mx)
        return mx
