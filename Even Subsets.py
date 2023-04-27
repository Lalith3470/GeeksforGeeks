class Solution:
	def countSumSubsets(self, arr, N):
		#Code here
		cnt=[]
		sm=0
		def subs(idx,arr,N,sm,cnt):
		    if idx>=N:
		        if sm%2==0:
		            c=[1]
		            cnt.append(c[:])
		        return
		    sm+=arr[idx]
		    subs(idx+1,arr,N,sm,cnt)
		    sm-=arr[idx]
		    subs(idx+1,arr,N,sm,cnt)
		subs(0,arr,N,sm,cnt)
		return len(cnt)-1
