class Solution:
	def removeDups(self, S):
		# code here
		s=""
		for i in S:
		    if i not in s:
		        s+=i
		return s

