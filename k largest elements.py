#User function Template for python3
class Solution:

	def kLargest(self,arr, n, k):
		# code here
		arr.sort(reverse=True)
		return arr[:k]
