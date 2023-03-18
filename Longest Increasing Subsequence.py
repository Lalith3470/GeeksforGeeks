
class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        dp=[1]*(n+1)
        mx=0
        for i in range(n):
            for j in range(i):
                if a[i]>a[j]:
                    dp[i]=max(dp[i],dp[j]+1)
            mx=max(mx,dp[i])
        return mx  
