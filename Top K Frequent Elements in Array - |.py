class Solution:
	def topK(self, nums, k):
		#Code here
		dict={}
		res=[]
		for x in nums:
		    if x in dict.keys():
		        dict[x]=dict[x]+1
		    else:
		        dict[x]=1
		d=sorted(dict.items(),key=lambda x: (x[1],x[0]),reverse=True)
		n=len(d)
		for i in range(min(n,k)):
		    res.append(d[i][0])
		    
		return res
