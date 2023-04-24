class Solution:
    def maxSquare(self, n, m, mat):
        # code here
        dp=[[0]*(m+1) for i in range(n+1)]
        mx=0
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1]=mat[i][j]
        mx=0
        for i in range(n+1):
            for j in range(m+1):
                if dp[i][j]==1:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                mx=max(dp[i][j],mx)
        return mx
