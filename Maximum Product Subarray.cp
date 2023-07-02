#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		mx=arr[0]
		st=1
		end=1
		for i in range(n):
		    if st==0:st=1
		    if end==0:end=1
		    end*=arr[n-i-1]
		    st*=arr[i]
		    mx=max(mx,end,st)
		return mx
