#User function Template for python3

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        lst=arr1+arr2
        lst.sort()
        arr1[:]=lst[:n]
        arr2[:]=lst[n:]
