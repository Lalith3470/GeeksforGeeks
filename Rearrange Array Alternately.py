#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        arr.sort()
        val=arr[::-1]
        lst=[]
        for i in range(n):
            lst.append(val[i])
            lst.append(arr[i])
        arr[:]=lst[:n]
