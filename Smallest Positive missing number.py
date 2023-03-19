class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        lst=[]
        for i in range(1,n+2):
            lst.append(i)
        val=sorted(set(lst)-set(arr))
        
        for i in val:return i
