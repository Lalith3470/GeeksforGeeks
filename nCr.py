from math import factorial
class Solution:
    def nCr(self, n, r):
        if n<r:return 0
        dp=[1]*(n+1)
        for i in range(2,n+1):
            dp[i]=dp[i-1]*i
        res=dp[n]//(dp[n-r]*dp[r]) 
        return res%1000000007
        
