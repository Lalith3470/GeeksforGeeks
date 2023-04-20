#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		def subs(idx,arr,N,lst,l):
            if idx>=N:
                l.append(lst[:])
                return
            lst.append(arr[idx])
            subs(idx+1,arr,N,lst,l)
            lst.pop()
            subs(idx+1,arr,N,lst,l)
            return
		lst=[]
		l=[]
		subs(0,arr,N,lst,l)
		v=[]
		for i in l:
		    v.append(sum(i))
		return v
