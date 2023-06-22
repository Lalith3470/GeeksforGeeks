class Solution:
	def minPoints(self, points, M, N):
		# code here
		dp=[[100000]*(N+1) for i in range(M+1)]
		dp[0][1]=1
		dp[1][0]=1
		lst=[i[::-1] for i in points]
		lst=lst[::-1]
	
		for i in range(1,M+1):
		    for j in range(1,N+1):
		        tmp=min(dp[i-1][j],dp[i][j-1])-lst[i-1][j-1]
		        dp[i][j]=max(tmp,1)
		 
		return dp[-1][-1]
