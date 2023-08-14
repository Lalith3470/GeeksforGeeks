from collections import Counter
class Solution:
	def singleNumber(self, nums):
		# Code here
		cnt=Counter(nums)
		return sorted([i for i,j in cnt.items() if j==1])
