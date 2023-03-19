class Solution:
    def editDistance(self, s, t):
        # Code here
        l1=len(s)
        l2=len(t)
        dp=[[0]*(l2+1) for i in range(l1+1)]
        mx=0
        for i in range(l1+1):
            for j in range(l2+1):
                if i==0:dp[i][j]=j
                elif j==0:dp[i][j]=i
                elif s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        return dp[-1][-1]
