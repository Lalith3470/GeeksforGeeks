#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def search(self,matrix, n, m, x): 
    	# code here 
    	for i in matrix:
    	    if x in i:
    	        return 1
    	return 0
    	
