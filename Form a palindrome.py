
class Solution:
    def countMin(self, Str):
        # code here
        tmp=Str[::-1]
        n=len(Str)
        dp=[[0]*(n+1) for i in range(n+1)]
        if tmp==Str:return 0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if Str[i-1]==tmp[j-1]: dp[i][j]=dp[i-1][j-1]+1
                else:dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return n-dp[-1][-1]
