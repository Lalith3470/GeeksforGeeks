class Solution:
	def maxSumIS(self, Arr, n):
		# code here
		dp = [0] * n
    for i in range(n):
        dp[i] = Arr[i]
        for j in range(i):
            if Arr[i] > Arr[j]:
                dp[i] = max(dp[i], dp[j] + Arr[i])
    return max(dp)
