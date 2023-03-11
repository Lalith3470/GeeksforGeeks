class Solution:
	def findMidSum(self, ar1, ar2, n): 
		# code here 
		final=ar1+ar2
		final.sort()
		return final[n]+final[n-1]
