from collections import Counter
class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	ans=Counter(arr)
    	lst=[]
    	for i,j in ans.items():
    	    if j>1:
    	        lst.append(i)
    	if not lst:
    	    return [-1]
    	lst.sort()
    	return lst
