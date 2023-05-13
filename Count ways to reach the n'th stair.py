class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-2]+dp[i-1]
        return dp[-1]%(10**9+7)
            
